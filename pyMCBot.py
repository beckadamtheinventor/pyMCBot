
import os, sys, math, socket, threading, time, struct, hashlib
from PacketID import PacketID
from NBT import NBT
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA

MC_DEFAULT_PORT = 25565
PROTOCOL_VERSION = 78

SIZEOF_BYTE  = 1
SIZEOF_SHORT = 2
SIZEOF_INT   = 4
SIZEOF_LONG  = 8
SIZEOF_DOUBLE= 8
SIZEOF_UUID  = 16
SIZEOF_ENTITYID = SIZEOF_INT


def __readByte(o, data=None):
	return o._receive_int(SIZEOF_BYTE, data=data)

def __readShort(o, data=None):
	return o._receive_int(SIZEOF_SHORT, data=data)

def __readInt(o, data=None):
	return o._receive_int(SIZEOF_INT, data=data)

def __readFloat(o, data=None):
	return o._receive_float(data)

def __readString(o, data=None):
	return o._receive_string(data)

def __readSlot(o, data=None):
	return o._receive_slot(data)

def __readIntVector(o, data=None):
	x = o._receive(SIZEOF_INT, data)
	y = o._receive(SIZEOF_INT, data)
	z = o._receive(SIZEOF_INT, data)
	return {"x": x, "y": y, "z": z}

def __readUnknown(o, data=None):
	if data is None:
		data = o._receive_all()
	o._debuglog(f"Skipping unknown data: 0x{''.join([hex(c//16)[2]+hex(c%16)[2] for c in data])} (big-endian)")

ENTITY_METADATA_VALUE_TYPE_READERS = {
	0: __readByte,
	1: __readShort,
	2: __readInt,
	3: __readFloat,
	4: __readString,
	5: __readSlot,
	6: __readIntVector,
	7: __readUnknown,
}


class Client:
	def __init__(self, debug=False):
		self._sock = socket.socket()
		self._sock.setblocking(True)
		self._packet_thread = None
		self._is_connected = False
		self._is_logged_in = False
		self.in_godmode = False
		self.can_fly = False
		self.is_flying = False
		self.in_creative_mode = False
		self._debug_mode = debug
		self._entities = {}
		self.worldage = None
		self.timeofday = None
		self._update = None
		self.last_packet_id = None
		self.set_locale()
		self.position = {"x": None, "y": None, "z": None}
		self.rotation = {"pitch": None, "yaw": None}
		self.equipment = {}
		self.inventory = {}
		self.tab_completed_string = None
		self.__packet = None
		self.__oldpackets = []
		self.log_file = os.path.join(os.path.dirname(__file__), f"{time.strftime('%a_%b_%d_%Y.%I-%M-%S%p')}.log")
		self.log_fd = open(self.log_file, 'w')

	def set_locale(self, locale="en_US"):
		self._locale = locale

	def debug_mode(self, debug=True):
		self.debug = debug

	def login(self, user, passwd=None, run=True):
		""" Log into a server and run the bot (unless run=False)"""
		self._infolog("Logging in...")
		self._send_packet(PacketID.HANDSHAKE, bytes([PROTOCOL_VERSION]),
			self._encode_string(user), self._encode_string(self.host), self.port.to_bytes(4, 'big'))
		self._debuglog("Sent handshake.")
		self._infolog("Waiting for login...")
		if run:
			self.run()
		return True


	def run(self):
		""" Start the bot's packet handling thread """
		self._packet_thread = threading.Thread(target=self._handle_packets)
		self._packet_thread.start()

	def dummy(self):
		""" Pause until the bot is disconnected or a keyboard interrupt is triggered """
		try:
			while self._is_connected:
				time.sleep(0.5)
		except KeyboardInterrupt:
			self._disconnect()

	def console(self):
		""" Run an interactive console until the bot is disconnected or a keyboard interrupt is triggered """
		try:
			while self._is_connected:
				cmd = input("> ")
				if " " in cmd:
					cmd, args = cmd.split()
				else:
					cmd, args = cmd, []
				if cmd in ("help", "h"):
					print("stop       | stop the bot")
				elif cmd in ("stop",):
					break
		except KeyboardInterrupt:
			pass
		print("Shutting down...")
		self._disconnect()
		time.sleep(1) # wait

	def is_handling_packets(self):
		""" Returns true if the server's packet thread is alive """
		if self._packet_thread is not None:
			return self._packet_thread.is_alive()
		return False

	def _handle_packets(self):
		while self._is_connected:
			if self._update is not None:
				self._update()
			try:
				self.handle_packet()
			except KeyboardInterrupt:
				break
			except TimeoutError:
				pass

	def get_packet(self, i=None):
		""" Return a previously processed packet or the current packet if no index is passed """
		if i is None:
			return self.__packet
		elif type(i) is int:
			return self.__oldpackets[i]
		raise ValueError("Argument must be a valid integer or None")

	def handle_packet(self):
		""" Handle a packet if a packet is available """
		if self._is_connected:
			packetid = self._receive_int(SIZEOF_BYTE, signed=False)

			if self.__packet is not None:
				self.__oldpackets.append(bytes(self.__packet))
			self.__packet = [packetid]

			self._debuglog(f"Got packet: {hex(packetid)}")
			self.last_packet_id = packetid
			if packetid == PacketID.KEEPALIVE:         # S<>C let the server know we're still listening
				number = self._receive_int(SIZEOF_INT)
				self._send_packet(PacketID.KEEPALIVE, number.to_bytes(SIZEOF_INT, 'big', signed=True))
			elif packetid == PacketID.LOGINREQUEST:    # S->C server response to handshake
				self._eid = self._receive_int(SIZEOF_INT)
				self._entities[self._eid] = {"equipment":self.equipment,"position":self.position,"rotation":self.rotation, "inventory":self.inventory}
				self._leveltype = self._receive_string()
				self._gamemode = self._receive_int(SIZEOF_BYTE)
				self._dimension = self._receive_int(SIZEOF_BYTE)
				self._difficulty = self._receive_int(SIZEOF_BYTE)
				self._receive_int(SIZEOF_BYTE) # unused field
				self._maxplayers = self._receive_int(SIZEOF_BYTE)
				self._is_logged_in = True
				self._infolog("Logged in.")
				self._debuglog("Sending Client Settings...")
				self._send_packet(PacketID.CLIENTSETTINGS, self._encode_string(self._locale), bytes([3, 9, 0, 0]))
				self._debuglog("Sent.")
			elif packetid == PacketID.DISCONNECT:
				reason = self._receive_string()
				try:
					self._debuglog(f"Disconnected. Reason: {reason}")
				except UnicodeEncodeError as e:
					self._debuglog(f"Disconnected. Reason: {self._bytes_to_str(reason)}")
				self._disconnect()
			elif packetid == PacketID.TIMEUPDATE:      # S->C when the world age/time updates
				self.worldage = self._receive_int(SIZEOF_LONG)
				self.timeofday = self._receive_int(SIZEOF_LONG)
			elif packetid == PacketID.ENTITYEQUIPMENT: # S->C when entity equipment changes
				eid = self._receive_int(SIZEOF_ENTITYID)
				if eid not in self._entities.keys():
					self._entities[eid] = \
						{"equipment":{},"position":{"x":None, "y":None, "z":None},"rotation":{"pitch":None,"yaw":None},"status":0}
				slot = self._receive_int(SIZEOF_SHORT)
				if "equipment" not in self._entities.keys():
					self._entities[eid]["equipment"] = {}
				self._entities[eid]["equipment"][slot] = self._receive_slot()
			elif packetid == PacketID.SPAWNPOSITION:   # S->C when player spawnpoint changes / is set
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_INT)
				z = self._receive_int(SIZEOF_INT)
				self._spawnpoint = {"x": x, "y": y, "z": z}
			elif packetid == PacketID.UPDATEHEALTH:    # S->C when player health/hunger/saturation changes
				self._health = self._receive_float()
				self._food = self._receive_int(SIZEOF_SHORT)
				self._saturation = self._receive_float()
			elif packetid == PacketID.RESPAWN:         # S->C when player respawns
				self._dimension = self._receive_int(SIZEOF_INT)
				self._difficulty = self._receive_int(SIZEOF_BYTE, signed=False)
				self._gamemode = self._receive_int(SIZEOF_BYTE, signed=False)
				self._worldheight = self._receive_int(SIZEOF_BYTE, signed=False)
				self._leveltype = self._receive_string()
			elif packetid == PacketID.PLAYERPOSANDLOOK: # S<>C when the player moves
				self.position["x"] = self._receive_double()
				self._stance = self._receive_double()
				self.position["y"] = self._receive_double()
				self.position["z"] = self._receive_double()
				self.rotation["yaw"] = self._receive_float()
				self.rotation["pitch"] = self._receive_float()
				self._on_ground = self._receive_int() > 0
			elif packetid == PacketID.HELDITEMCHANGE:   # S<>C when held item slot changes
				self._hotbar_selection = self._receive_int(SIZEOF_SHORT)
			elif packetid == PacketID.USEBED:           # S->C when an entity goes to sleep
				eid = self._receive_int(SIZEOF_INT)
				self._receive_int(SIZEOF_BYTE, signed=False) # probably unused field
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_BYTE, signed=False)
				z = self._receive_int(SIZEOF_INT)
			elif packetid == PacketID.ANIMATION:         # S->C when an animation happens
				eid = self._receive_int(SIZEOF_INT)
				if eid not in self._entities.keys():
					self._entities[eid] = {}
				self._entities[eid]["animation"] = self._receive_int(SIZEOF_BYTE, signed=False)
			elif packetid == PacketID.SPAWNNAMEDENTITY:  # S->C when a named entity spawns
				eid = self._receive_int(SIZEOF_INT)
				name = self._receive_string()
				x = self._receive_fixed(SIZEOF_INT)
				y = self._receive_fixed(SIZEOF_INT)
				z = self._receive_fixed(SIZEOF_INT)
				yaw = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				pitch = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				helditem = self._receive_int(SIZEOF_SHORT, signed=False)
				metadata = self._receive_metadata()
				if eid not in self._entities.keys():
					self._entities[eid] = {}
				self._entities[eid]["name"] = name
				self._entities[eid]["position"] = {"x": x, "y": y, "z": z}
				self._entities[eid]["rotation"] = {"pitch": pitch, "yaw": yaw}
				self._entities[eid]["helditem"] = helditem
				self._entities[eid]["metadata"] = metadata
			elif packetid == PacketID.COLLECTITEM:      # S->C trigger item collection animation
				itemeid = self._receive_int(SIZEOF_INT)
				eid = self._receive_int(SIZEOF_INT)
			elif packetid == PacketID.SPAWNOBJECT:  # S-C Spawn an object/vehicle
				eid = self._receive_int(SIZEOF_INT)
				_type = self._receive_int(SIZEOF_BYTE)
				self._debuglog(f"Spawning entity type {_type} with ID {eid}")
				x = self._receive_fixed(SIZEOF_INT)
				y = self._receive_fixed(SIZEOF_INT)
				z = self._receive_fixed(SIZEOF_INT)
				yaw = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				pitch = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				objectdata = self._receive_objectdata()
			elif packetid == PacketID.SPAWNMOB:     # S->C Spawn a mob
				eid = self._receive_int(SIZEOF_INT)
				_type = self._receive_int(SIZEOF_BYTE)
				x = self._receive_fixed(SIZEOF_INT)
				y = self._receive_fixed(SIZEOF_INT)
				z = self._receive_fixed(SIZEOF_INT)
				pitch = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				headpitch = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				yaw = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				vx = self._receive_int(SIZEOF_SHORT)
				vy = self._receive_int(SIZEOF_SHORT)
				vz = self._receive_int(SIZEOF_SHORT)
				self._debuglog(f"Spawning mob {eid} of type {_type} at {x}, {y}, {z}")
				metadata = self._receive_metadata()
				self._entities[eid] = {"type":_type, "position":{"x": x, "y": y, "z": z},
					"rotation":{"pitch":pitch, "yaw":yaw}, "headpitch": headpitch,
					"velocity":{"x": vx, "y": vy, "z": vz}, "metadata": metadata, "status": 0}
			elif packetid == PacketID.SPAWNPAINTING: # S->C Spawn a painting
				eid = self._receive_int(SIZEOF_INT)
				title = self._receive_string()
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_INT)
				z = self._receive_int(SIZEOF_INT)
				direction = self._receive_int(SIZEOF_INT)
				self._entities[eid] = {"type": "painting", "position": {"x": x, "y": y, "z": z},
					"direction": direction, "title": title}
			elif packetid == PacketID.SPAWNEXPORB:  # S->C Spawn an experience orb
				eid = self._receive_int(SIZEOF_INT)
				x = self._receive_fixed(SIZEOF_INT)
				y = self._receive_fixed(SIZEOF_INT)
				z = self._receive_fixed(SIZEOF_INT)
				count = self._receive_int(SIZEOF_SHORT)
				self._entities[eid] = {"type": "experience", "position": {"x": x, "y": y, "z": z},
					"count": count}
			elif packetid == PacketID.ENTITYVELOCITY: # S->C Set an entity's velocity
				eid = self._receive_int(SIZEOF_INT)
				vx = self._receive_int(SIZEOF_SHORT)
				vy = self._receive_int(SIZEOF_SHORT)
				vz = self._receive_int(SIZEOF_SHORT)
				if eid in self._entities.keys(): # sanity-check if we know this entity exists yet
					self._entities[eid]["velocity"] = {"x": vx, "y": vy, "z": vz}
			elif packetid == PacketID.DESTROYENTITY: # S->C Destroy an entity
				count = self._receive_int(SIZEOF_BYTE)
				for i in range(count):
					eid = self._receive_int(SIZEOF_INT)
					if eid in self._entities.keys():
						del self._entities[eid]
			elif packetid == PacketID.ENTITY:        # S->C Initialize an entity if it hasn't been initialized yet
				eid = self._receive_int(SIZEOF_INT)
				if eid not in self._entities.keys():
					self._entities[eid] = \
						{"equipment":{},"position":{"x":None, "y":None, "z":None},"rotation":{"pitch":None,"yaw":None}}
			elif packetid == PacketID.ENTITYRELMOVE: # S->C Sent when an entity travels less than 4 blocks
				eid = self._receive_int(SIZEOF_INT)
				dx = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
				dy = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
				dz = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
				if eid in self._entities.keys():
					pos = self._entities[eid]["position"]
					pos["x"] += dx
					pos["y"] += dy
					pos["z"] += dz
			elif packetid == PacketID.ENTITYLOOK:   #S->C Sent when an entity rotates
				eid = self._receive_int(SIZEOF_INT)
				yaw = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				pitch = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				if eid in self._entities.keys():
					self._entities[eid]["rotation"] = {"pitch":pitch, "yaw":yaw}
			elif packetid == PacketID.ENTITYLOOKANDRELMOVE:   #S->C Sent when an entity moves less than 4 blocks and rotates
				eid = self._receive_int(SIZEOF_INT)
				dx = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
				dy = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
				dz = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
				yaw = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				pitch = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				if eid in self._entities.keys():
					self._entities[eid]["rotation"] = {"pitch":pitch, "yaw":yaw}
					pos = self._entities[eid]["position"]
					pos["x"] += dx
					pos["y"] += dy
					pos["z"] += dz
			elif packetid == PacketID.ENTITYTELEPORT:        # S->C Sent when an entity moves more than 4 blocks
				eid = self._receive_int(SIZEOF_INT)
				x = self._receive_fixed(SIZEOF_INT)
				y = self._receive_fixed(SIZEOF_INT)
				z = self._receive_fixed(SIZEOF_INT)
				yaw = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				pitch = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				if eid in self._entities.keys():
					self._entities[eid]["rotation"] = {"pitch":pitch, "yaw":yaw}
					self._entities[eid]["position"] = {"x": x, "y": y, "z": z}
			elif packetid == PacketID.ENTITYHEADLOOK:       # S->C Sent to change the direction an entity's head is facing
				eid = self._receive_int(SIZEOF_INT)
				yaw = self._receive_int(SIZEOF_BYTE, signed=False)/(math.pi/128)
				if eid in self._entities.keys():
					self._entities[eid]["headyaw"] = yaw
			elif packetid == PacketID.ENTITYSTATUS:         # S->C Set the status of an entity
				eid = self._receive_int(SIZEOF_INT)
				status = self._receive_int(SIZEOF_BYTE)
				if eid in self._entities.keys():
					self._entities[eid]["status"] = status
			elif packetid == PacketID.ATTACHENTITY:         # S->C Attach an entity to another entity
				eid = self._receive_int(SIZEOF_INT)
				vid = self._receive_int(SIZEOF_INT)
				leash = self._receive_int(SIZEOF_INT)
				if eid in self._entities.keys():
					self._entities[eid]["attachedto"] = vid
					if leash:
						self._entities[eid]["leashedto"] = vid
			elif packetid == PacketID.ENTITYMETADATA:
				self._debuglog("Receiving Entity Metadata packet")
				eid = self._receive_int(SIZEOF_INT)
				metadata = self._receive_metadata()
				if eid in self._entities.keys():
					self._entities[eid]["metadata"] = metadata
			elif packetid == PacketID.ENTITYEFFECT:        # S->C Add an effect to an entity
				eid = self._receive_int(SIZEOF_INT)
				effect = self._receive_int(SIZEOF_INT)
				amplifier = self._receive_int(SIZEOF_BYTE)
				duration = self._receive_int(SIZEOF_SHORT)
				if eid in self._entities.keys():
					if "effects" not in self._entities[eid].keys():
						self._entities[eid]["effects"] = []
					self._entities[eid]["effects"].append({"effect": effect, "duration": duration, "amplifier": amplifier})
			elif packetid == PacketID.REMOVEENTITYEFFECT:  # S->C Remove an effect ID on an entity.
				eid = self._receive_int(SIZEOF_INT)
				effect = self._receive_int(SIZEOF_INT)
				if eid in self._entities.keys():
					if "effects" in self._entities[eid].keys():
						i = 0
						while i < len(self._entities[eid]["effects"]):
							if self._entities[eid]["effects"][i]["effect"] == effect:
								self._entities[eid]["effects"].pop(i)
							else:
								i += 1
			elif packetid == PacketID.SETEXPERIENCE:       # S->C Set a player's experience levels et al
				self._experiencebar = self._receive_float()
				self._experiencelevel = self._receive_int(SIZEOF_SHORT)
				self._totalexperience = self._receive_int(SIZEOF_SHORT)
			elif packetid == PacketID.ENTITYPROPERTIES:    # S->C Set an entity's properties. TODO: Actually make this do stuff
				eid = self._receive_int(SIZEOF_INT)
				numproperties = self._receive_int(SIZEOF_INT)
				self._debuglog(f"Setting {numproperties} entity properties for {eid}")
				for i in range(numproperties):
					key = self._receive_string()
					value = self._receive_double()
					modifierslen = self._receive_int(SIZEOF_SHORT)
					self._debuglog(f"Setting {modifierslen} modifiers on value {value} for key {key}")
					for j in range(modifierslen):
						uuid = self._receive(SIZEOF_UUID)
						amount = self._receive_double()
						operation = self._receive_int(SIZEOF_BYTE, signed=False)
						self._debuglog(f"UUID: 0x{''.join([hex(c//16)[2]+hex(c%16)[2] for c in uuid])} (big-endian)")
						self._debuglog(f"amount: {amount}")
						self._debuglog(f"operation: {operation}")
			elif packetid == PacketID.CHUNKDATA:         # S->C Sent chunk data
				cx = self._receive_int(SIZEOF_INT)
				cz = self._receive_int(SIZEOF_INT)
				groundupcontinuous = self._receive_int(SIZEOF_BYTE)
				primarybitmap = self._receive_int(SIZEOF_SHORT, signed=False)
				addbitmap = self._receive_int(SIZEOF_SHORT, signed=False)
				compresseddatalen = self._receive_int(SIZEOF_INT)
				compresseddata = self._receive(compresseddatalen)
			elif packetid == PacketID.MULTIBLOCKCHANGE:
				cx = self._receive_int(SIZEOF_INT)
				cz = self._receive_int(SIZEOF_INT)
				recordcount = self._receive_int(SIZEOF_SHORT)
				datasize = self._receive_int(SIZEOF_INT)
				records = self._receive(recordcount*4)
			elif packetid == PacketID.BLOCKCHANGE:
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_BYTE, signed=False)
				z = self._receive_int(SIZEOF_INT)
				blocktype = self._receive_int(SIZEOF_SHORT)
				blockmetadata = self._receive_int(SIZEOF_BYTE)
			elif packetid == PacketID.BLOCKACTION:
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_SHORT)
				z = self._receive_int(SIZEOF_INT)
				b1 = self._receive_int(SIZEOF_BYTE)
				b2 = self._receive_int(SIZEOF_BYTE)
			elif packetid == PacketID.BLOCKBREAKANIMATION:
				eid = self._receive_int(SIZEOF_INT)
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_SHORT)
				z = self._receive_int(SIZEOF_INT)
				destroystage = self._receive_int(SIZEOF_BYTE)
			elif packetid == PacketID.MAPCHUNKBULK:
				chunkcount = self._receive_int(SIZEOF_SHORT)
				datalen = self._receive_int(SIZEOF_INT)
				skylightsent = self._receive_int(SIZEOF_BYTE)
				data = self._receive(datalen)
				for i in range(chunkcount):
					cx = self._receive_int(SIZEOF_INT)
					cz = self._receive_int(SIZEOF_INT)
					primarybitmap = self._receive_int(SIZEOF_SHORT)
					addbitmap = self._receive_int(SIZEOF_SHORT)
			elif packetid == PacketID.EXPLOSION:
				x = self._receive_double()
				y = self._receive_double()
				z = self._receive_double()
				radius = self._receive_float()
				recordcount = self._receive_int(SIZEOF_INT)
				records = []
				for i in range(recordcount):
					dx = self._receive_int(SIZEOF_BYTE)
					dy = self._receive_int(SIZEOF_BYTE)
					dz = self._receive_int(SIZEOF_BYTE)
					records.append([dx, dy, dz])
				playermotionx = self._receive_float()
				playermotiony = self._receive_float()
				playermotionz = self._receive_float()
			elif packetid == PacketID.SOUNDORPARTICLEEFFECT:
				effectid = self._receive_int(SIZEOF_INT)
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_BYTE, signed=False)
				z = self._receive_int(SIZEOF_INT)
				data = self._receive_int(SIZEOF_INT)
				disablerelativevolume = self._receive_int(SIZEOF_BYTE)
			elif packetid == PacketID.NAMEDSOUNDEFFECT:
				soundname = self._receive_string()
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_INT)
				z = self._receive_int(SIZEOF_INT)
				volume = self._receive_float()
				pitch = self._receive_int(SIZEOF_BYTE) # 63 = 100%
			elif packetid == PacketID.PARTICLE:
				particlename = self._receive_string()
				x = self._receive_float()
				y = self._receive_float()
				z = self._receive_float()
				ox = self._receive_float()
				oy = self._receive_float()
				oz = self._receive_float()
				speed = self._receive_float()
				number = self._receive_int(SIZEOF_INT)
			elif packetid == PacketID.CHANGEGAMESTATE:
				reason = self._receive_int(SIZEOF_BYTE)
				gamemode = self._receive_int(SIZEOF_BYTE)
				if reason == 1:
					self._is_raining = True
				elif reason == 2:
					self._is_raining = False
				elif reason == 3:
					self._gamemode = gamemode
			elif packetid == PacketID.SPAWNGLOBALENTITY:
				entityid = self._receive_int(SIZEOF_INT)
				entitytype = self._receive_int(SIZEOF_BYTE)
				x = self._receive_fixed(SIZEOF_INT)
				y = self._receive_fixed(SIZEOF_INT)
				z = self._receive_fixed(SIZEOF_INT)
			elif packetid == PacketID.OPENWINDOW:
				windowid = self._receive_int(SIZEOF_BYTE, signed=False)
				windowtype = self._receive_int(SIZEOF_BYTE, signed=False)
				if windowtype not in (73,):
					windowtitle = self._receive_string()
					numberofslots = self._receive_int(SIZEOF_BYTE)
				else:
					windowtitle = ""
					numberofslots = 0
				useprovidedwindowtitle = self._receive_int(SIZEOF_BYTE)
				self._debuglog(f"Opening Window ID {windowid} type {windowtype} title \"{windowtitle}\" slots {numberofslots} using provided title? {useprovidedwindowtitle}")
				if windowtype == 11: # AnimalChest
					entityid = self._receive_int(SIZEOF_INT)
			elif packetid == PacketID.CLOSEWINDOW:
				windowid = self._receive_int(SIZEOF_BYTE, signed=False)
			elif packetid == PacketID.SETSLOT:
				windowid = self._receive_int(SIZEOF_BYTE, signed=False)
				slot = self._receive_int(SIZEOF_SHORT)
				slotdata = self._receive_slot()
			elif packetid == PacketID.SETWINDOWITEMS:
				windowid = self._receive_int(SIZEOF_BYTE, signed=False)
				count = self._receive_int(SIZEOF_SHORT)
				slots = []
				for i in range(count):
					slots.append(self._receive_slot())
			elif packetid == PacketID.UPDATEWINDOWPROPERTY:
				windowid = self._receive_int(SIZEOF_BYTE, signed=False)
				prop = self._receive_int(SIZEOF_SHORT)
				value = self._receive_int(SIZEOF_SHORT)
			elif packetid == PacketID.CONFIRMTRANSACTION:
				windowid = self._receive_int(SIZEOF_BYTE, signed=False)
				actionnumber = self._receive_int(SIZEOF_SHORT)
				accepted = self._receive_int(SIZEOF_BYTE)
			elif packetid == PacketID.CREATIVEINVENTORYACTION:
				slot = self._receive_int(SIZEOF_SHORT)
				item = self._receive_slot()
			elif packetid == PacketID.UPDATESIGN:
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_SHORT)
				z = self._receive_int(SIZEOF_INT)
				line1 = self._receive_string()
				line2 = self._receive_string()
				line3 = self._receive_string()
				line4 = self._receive_string()
			elif packetid == PacketID.ITEMDATA:
				itemtype = self._receive_int(SIZEOF_SHORT)
				itemid = self._receive_int(SIZEOF_SHORT)
				datalen = self._receive_int(SIZEOF_SHORT)
				data = self._receive(datalen)
			elif packetid == PacketID.UPDATETILEENTITY:
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_SHORT)
				z = self._receive_int(SIZEOF_INT)
				action = self._receive_int(SIZEOF_BYTE)
				datalen = self._receive_int(SIZEOF_SHORT)
				if datalen > 0:
					data = self._receive(datalen)
			elif packetid == PacketID.TILEEDITOROPEN:
				tileentityid = self._receive_int(SIZEOF_BYTE)
				x = self._receive_int(SIZEOF_INT)
				y = self._receive_int(SIZEOF_INT)
				z = self._receive_int(SIZEOF_INT)
			elif packetid == PacketID.INCREMENTSTATISTIC:
				statid = self._receive_int(SIZEOF_INT)
				amount = self._receive_int(SIZEOF_INT)
			elif packetid == PacketID.PLAYERLISTITEM:
				name = self._receive_string()
				online = self._receive_int(SIZEOF_BYTE)
				ping = self._receive_int(SIZEOF_SHORT)
			elif packetid == PacketID.PLAYERABILITIES:
				flags = self._receive_int(SIZEOF_BYTE)
				self.in_godmode = (flags & 8) != 0
				self.can_fly = (flags & 4) != 0
				self.is_flying = (flags & 2) != 0
				self.in_creative_mode = (flags & 1) != 0
				self._flyingspeed = self._receive_float()
				self._walkingspeed = self._receive_float()
			elif packetid == PacketID.TABCOMPLETE:
				self.tab_completed_string = self._receive_string()
			elif packetid == PacketID.SCOREBOARDOBJECTIVE:
				objectivename = self._receive_string()
				objectivevalue = self._receive_string()
				createremove = self._receive_int(SIZEOF_BYTE) # 0 to create, 1 to remove, 2 to update display text
			elif packetid == PacketID.UPDATESCORE:
				itemname = self._receive_string()
				updateremove = self._receive_int(SIZEOF_BYTE) # 0 to create/update, 1 to remove
				if updateremove != 1:
					scorename = self._receive_string()
					value = self._receive_int()
			elif packetid == PacketID.DISPLAYSCOREBOARD:
				position = self._receive_int(SIZEOF_BYTE) # 0 = list, 1 = sidebar, 2 = belowName
				scorename = self._receive_string()
			elif packetid == PacketID.TEAMS:
				teamname = self._receive_string()
				# 0->create team, 1->remove team, 2->update information, 3->add players, 4->remove players
				mode = self._receive_int(SIZEOF_BYTE)
				if mode in (0, 2):
					teamdisplayname = self._receive_string()
					teamprefix = self._receive_string()
					teamsuffix = self._receive_string()
					friendlyfire = self._receive_int(SIZEOF_BYTE)
				if mode in (0, 3, 4):
					playercount = self._receive_int(SIZEOF_SHORT)
					players = []
					for i in range(playercount):
						players.append(self._receive_string())
			elif packetid == PacketID.PLUGINMESSAGE:
				channel = self._receive_string()
				datalen = self._receive_int(SIZEOF_SHORT)
				data = self._receive(datalen)
			elif packetid == PacketID.ENCRYPTIONKEYREQUEST: # S->C Server sends serverid, pubkey, and verifytoken
				self._serverid = self._receive_string()
				self._serverpubkeylen = self._receive_int(SIZEOF_SHORT)
				self._serverpubkey = self._receive(self._serverpubkeylen)
				self._verifytokenlen = self._receive_int(SIZEOF_SHORT)
				self._verifytoken = self._receive(self._verifytokenlen)

				# self._serverpubkey =  RSA.import_key(self._serverpubkey)
				# print(self._serverid, self._serverpubkey, self._verifytoken, sep="\n\n")

				# sharedsecret = os.urandom(16)
				# cipher = PKCS1_v1_5.new(self._serverpubkey)
				# cipheredsecret = cipher.encrypt(sharedsecret)
				# cipheredverifytoken = cipher.encrypt(self._verifytoken)
				# print(cipheredsecret)
				# print(cipheredverifytoken)
				# self._send_packet(PacketID.ENCRYPTIONKEYRESPONSE, len(cipheredsecret).to_bytes(SIZEOF_SHORT, 'big'), cipheredsecret, len(cipheredverifytoken).to_bytes(SIZEOF_SHORT, 'big'), cipheredverifytoken)

				if not self._is_logged_in:
					self._debuglog("Sending Client Statuses...")
					self._send_packet(PacketID.CLIENTSTATUSES, 0) # tell the server we're ready to spawn
					self._debuglog("Sent.")
					# print("Sending Client Settings...")
					# self._send_packet(PacketID.CLIENTSETTINGS, self._encode_string(self._locale), 3, 9, 3, 1)
					# print("Sent.")

	def connect(self, addr=None, port=MC_DEFAULT_PORT):
		if addr is None:
			if self._is_connected:
				self.logout()
		else:
			if ":" in addr:
				addr, port = addr.rsplit(":", maxsplit=1)
				try:
					port = int(port)
				except ValueError as e:
					self._errorlog("Port must be a valid integer.")
					raise e
			self.host = addr
			self.port = port
			self._connect(addr, port)

	def disconnect(self):
		if self._is_connected:
			self.logout()

	def message(self, message):
		pass

	def _connect(self, addr, port=MC_DEFAULT_PORT):
		self._sock.connect((addr, port))
		self._is_connected = True

	def _disconnect(self):
		self._send_packet(PacketID.DISCONNECT)

		self._is_logged_in = False

		# wait for the packet handling thread to complete
		while self.is_handling_packets():
			time.sleep(0.05)

		self._is_connected = False
		self._sock.close()

	def _errorlog(self, *args):
		self.__logwrite("[E]", " ".join([str(arg) for arg in args]))

	def _warning(self, *args):
		self.__logwrite("[W]", " ".join([str(arg) for arg in args]))

	def _infolog(self, *args):
		self.__logwrite("[I]:", " ".join([str(arg) for arg in args]))

	def _debuglog(self, *args):
		if self._debug_mode:
			self.__logwrite("[D]", " ".join([str(arg) for arg in args]))

	def __logwrite(self, *args):
		s = " ".join([arg for arg in args])
		print(s)
		self.log_fd.write(s)
		self.log_fd.write("\n")

	def read(self, amt=1):
		return self._receive(amt)

	def _receive_metadata(self, data=None):
		metadata = []
		while True:
			item = self._receive_int(SIZEOF_BYTE, signed=False, data=data)
			if item == 0x7F:
				return metadata
			key, _type = item & 0x1F, item // 2**5
			self._debuglog(f"Reading entity metadata type: {_type} with key {key}")
			if _type in ENTITY_METADATA_VALUE_TYPE_READERS.keys():
				reader = ENTITY_METADATA_VALUE_TYPE_READERS[_type]
				value = reader(self, data)
				metadata.append({"key": key, "value": value, "type": _type})
			else:
				self._errorlog(f"Received invalid entity metadata key {key} type {_type}")
				raise ValueError(f"Invalid entity metadata received: key {key} type {_type} ({hex(item)})")

	def _receive_slot(self, data=None):
		c = self._receive_int(SIZEOF_SHORT, data=data)
		self._debuglog("receiving slot...")
		self._debuglog(f"slot number: {c}")
		if c > 0:
			itemid = self._receive_int(SIZEOF_SHORT, data=data)
			self._debuglog(f"Item ID: {hex(itemid)}")
			if itemid != -1:
				itemcount = self._receive_int(SIZEOF_BYTE, data=data)
				itemdamage = self._receive_int(SIZEOF_SHORT, data=data)
				if itemcount > 0:
					nbtsize = self._receive_int(SIZEOF_SHORT, data=data)
					self._debuglog(f"count: {itemcount} damage: {itemdamage} nbt bytes: {nbtsize}")
					if nbtsize == -1:
						nbtsize = 0
					if nbtsize > 0:
						nbt = NBT(self._receive(nbtsize, data=data))
					else:
						nbt = None
					return {"id": itemid, "count": itemcount, "nbt": nbt}
			return {"id": -1, "count": -1, "nbt": None}
		else:
			return None

	def _receive_int(self, amt=1, signed=True, data=None):
		return int.from_bytes(self._receive(amt, data=data), 'big', signed=signed)

	def _receive_fixed(self, amt=1, signed=True, fractionalbits=5):
		return self._receive_int(amt, signed) / (2 ** fractionalbits)

	def _receive_float(self, data=None):
		if data is None:
			return self._decode_float(self._receive(4))
		else:
			return self._decode_float(bytes(data)[:4])

	def _receive_double(self, data=None):
		if data is None:
			return self._decode_double(self._receive(8))
		else:
			return self._decode_double(bytes(data)[:8])

	def _receive_varlong(self, data=None):
		return self._receive_varint(data)

	def _receive_varint(self, data=None):
		e = 1
		num = 0
		if data is None:
			while True:
				c = self._receive_int(SIZEOF_BYTE, data=data)
				num |= (c & 0x7F) * e
				if not c & 0x80:
					return num
		else:
			i = 0
			while True:
				c = data[i]
				num |= (c & 0x7F) * e
				if not c & 0x80:
					return num
				i += 1

	def _receive_string(self, data=None):
		num = self._receive_int(SIZEOF_SHORT, signed=False, data=data)
		if data is None:
			return self._bytes_to_str(self._receive(num * 2, data=data))
		else:
			return self._bytes_to_str(data[:num*2])

	def _receive_objectdata(self, data=None):
		intfield = self._receive_int(SIZEOF_INT, data=data)
		if intfield == 0:
			return {"intfield": intfeild}
		x = self._receive_int(SIZEOF_SHORT, data=data)
		y = self._receive_int(SIZEOF_SHORT, data=data)
		z = self._receive_int(SIZEOF_SHORT, data=data)
		return {"intfield": intfield, "velocity": {"x": x, "y": y, "z": z}}

	def _receive(self, amt=1, data=None):
		data = self.__receive(amt, data)
		if self.__packet is not None:
			if type(data) is bytes:
				self.__packet.extend(list(data))
			else:
				self.__packet.append(data & 0xff)
		return data

	def _receive_all(self):
		chunks = []
		while True:
			data = self._sock.recv(2048)
			if not data:
				return b''.join(data)
			chunks.append(data)

	def __receive(self, amt, data):
		if self._is_connected:
			if data is None:
				bytes_recd = 0
				chunks = []
				while bytes_recd < amt:
					chunk = self._sock.recv(min(amt - bytes_recd, 2048))
					if chunk == b'':
						# self._errorlog("Socket Connection Broken")
						# raise RuntimeError("socket connection broken")
						return b''.join(chunks)
					chunks.append(chunk)
					bytes_recd = bytes_recd + len(chunk)
				return b''.join(chunks)
			else:
				o = []
				for i in range(amt):
					o.append(data.pop(0))
				return bytes(o)
		else:
			return b''

	def _send(self, *args):
		for data in args:
			totalsent = 0
			while totalsent < len(data):
				sent = self._sock.send(data[totalsent:])
				if sent == 0:
					self._errorlog("Socket Connection Broken")
					raise RuntimeError("socket connection broken")
				totalsent = totalsent + sent

	def _send_packet(self, packetid, *args):
		o = [packetid]
		for arg in args:
			if type(arg) is bytes:
				o.extend(list(arg))
			elif type(arg) is int:
				o.append(arg)
			elif type(arg) is str:
				o.extend(self._str_to_bytes(arg))
		self._debuglog("Sending packet:", o)
		self._send(bytes(o))

	def _encode_string(self, data):
		return len(data).to_bytes(2, 'big', signed=False) + self._str_to_bytes(data)

	def _encode_varlong(self, num):
		return self._encode_varint(self, num)

	def _encode_varint(self, num):
		o = []
		while True:
			o.append((num & 0x7F) | 0x80)
			if num < 0x80:
				return bytes(o)
			num //= 0x80

	def _str_to_bytes(self, data):
		o = []
		for c in data:
			o.append(ord(c) // 256)
			o.append(ord(c) % 256)
		return bytes(o)

	def _bytes_to_str(self, data):
		o = []
		i = 0
		while i < min(len(data), 32767):
			c = data[i+1] + data[i]*256
			if c in range(128):
				o.append(chr(c))
			else:
				o.append(f"\\{hex(c)[1:]}")
			i += 2
		return "".join(o)

	def _decode_float(self, data):
		self._debuglog(f"Unpacking float from 0x{''.join([hex(c//16)[2]+hex(c%16)[2] for c in data])} (big-endian)")
		try:
			n = struct.unpack('>f', data)[0]
			self._debuglog(f"Unpacked float {n}")
			return n
		except struct.error:
			self._warning(f"[_decode_float] Failed to unpack float from data: 0x{''.join([hex(c//16)[2]+hex(c%16)[2] for c in data])} (big-endian)")

	def _decode_double(self, data):
		self._debuglog(f"[_decode_double] Unpacking double from 0x{''.join([hex(c//16)[2]+hex(c%16)[2] for c in data])} (big-endian)")
		try:
			n = struct.unpack('>d', data)[0]
			self._debuglog(f"[_decode_double] Unpacked double {n}")
			return n
		except struct.error:
			self._warning(f"[_decode_double] Failed to unpack double from data: 0x{''.join([hex(c//16)[2]+hex(c%16)[2] for c in data])} (big-endian)")


if __name__=='__main__':
	debug = False
	address = None
	port = MC_DEFAULT_PORT
	username = None
	passwd = None
	if len(sys.argv) > 1:
		for i in range(1, len(sys.argv)):
			if sys.argv[i] in ("-d", "--debug"):
				debug = True
			elif sys.argv[i] in ("-a", "--address", "--host"):
				if i+1 < len(sys.argv):
					address = sys.argv[i+1]
			elif sys.argv[i] in ("-p", "--port"):
				if i+1 < len(sys.argv):
					port = sys.argv[i+1]
			elif sys.argv[i] in ("-u", "--user"):
				if i+1 < len(sys.argv):
					username = sys.argv[i+1]
			elif sys.argv[i] in ("-w", "--passwd"):
				if i+1 < len(sys.argv):
					passwd = sys.argv[i+1]
	
	if username is None or address is None:
		print("""Usage:
 -d          | enable debug mode.
 -a addr     | server address to connect to.
 -p port     | server port. defaults to 25565.
 -u username | player username.
 -w password | player password. (not used yet)
""")
	else:
		client = Client(debug=debug)
		client.connect(address, port)
		if client.login(username, passwd):
			client.console()

