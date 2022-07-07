import gzip
import json
import math
import os
import socket
import sys
import threading
import time

from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA

if __name__ == '__main__':
    from packet import PacketID
    from event import Event
    from nbt import NBT
    from smpmap.smpmap import *
    from blocks import Blocks
else:
    from .packet import PacketID
    from .event import Event
    from .nbt import NBT
    from .smpmap.smpmap import *
    from .blocks import Blocks

MC_DEFAULT_PORT = 25565
PROTOCOL_VERSION = 78

SIZEOF_BYTE = 1
SIZEOF_SHORT = 2
SIZEOF_INT = 4
SIZEOF_LONG = 8
SIZEOF_DOUBLE = 8
SIZEOF_UUID = 16
SIZEOF_ENTITYID = SIZEOF_INT


def __read_byte(o, data=None):
    return o._receive_int(SIZEOF_BYTE, data=data)


def __read_short(o, data=None):
    return o._receive_int(SIZEOF_SHORT, data=data)


def __read_int(o, data=None):
    return o._receive_int(SIZEOF_INT, data=data)


def __read_float(o, data=None):
    return o._receive_float(data)


def __read_string(o, data=None):
    return o._receive_string(data)


def __read_slot(o, data=None):
    return o._receive_slot(data)


def __read_int_vector(o, data=None):
    x = o._receive(SIZEOF_INT, data)
    y = o._receive(SIZEOF_INT, data)
    z = o._receive(SIZEOF_INT, data)
    return {"x": x, "y": y, "z": z}


def __read_unknown(o, data=None):
    if data is None:
        data = o._receive_all()
    o._debuglog(f"Skipping unknown data: 0x{''.join([hex(c // 16)[2] + hex(c % 16)[2] for c in data])} (big-endian)")


ENTITY_METADATA_VALUE_TYPE_READERS = {
    0: __read_byte,
    1: __read_short,
    2: __read_int,
    3: __read_float,
    4: __read_string,
    5: __read_slot,
    6: __read_int_vector,
    7: __read_unknown,
}


class Client:
    def __init__(self, debug=False):
        self.port = None
        self.host = None
        self._locale = None
        self.main_thread = None
        self.uptime = 0
        self._debug_mode = debug
        self._packet_log_mode = False
        self._packet_thread = None
        self.is_running = False
        self.is_logged_in = False
        self.is_waiting_to_spawn = True
        self._outbound_encryption_enabled = False
        self._inbound_encryption_enabled = False
        self.in_godmode = False
        self.can_fly = False
        self.is_flying = False
        self.in_creative_mode = False
        self.can_move = False
        self.can_run = False
        self._has_sent_respawn = False
        self._entities = {}
        self.username = None
        self.worldage = None
        self.timeofday = None
        self._update = None
        self.eid = None
        self.metadata = {}
        self._entity_status = 0
        self.last_packet_id = None
        self.position = {"x": 0.0, "y": 0.0, "z": 0.0}
        self.velocity = {"x": 0.0, "y": 0.0, "z": 0.0}
        self.stance_offset = 1.62
        self.spawn_position = {"x": 0.0, "y": 0.0, "z": 0.0}
        self.rotation = {"pitch": 0.0, "yaw": 0.0}
        self.flying_speed = 0.02
        self.walking_speed = 0.1
        self.walking_time = 0
        self._walk_velocity = (0, 0)
        self.bounding_box = ((-0.5, 0, -0.5), (0.5, self.stance_offset, 0.5))
        self.gamemode = 0
        self.difficulty = 0
        self.dimension = 0
        self.health = 20.0
        self.food = None
        self.saturation = None
        self.equipment = {}
        self.inventory = {}
        self.tab_completed_string = None
        self._event_handlers = {}
        self.__event_queue = []
        self.__packetqueue = []
        self.__packet = None
        self.__oldpackets = []

        self._world = World()

        self._decrypt_cipher = None
        self._encrypt_cipher = None
        self.set_locale()
        self._userupdate = None

    def _init_logging(self):
        self.lock.acquire(blocking=True)
        self.log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs",
                                     f"{time.strftime('%a_%b_%d_%Y.%I-%M-%S%p')}.log")
        if os.path.exists(os.path.dirname(self.log_file)):
            if not os.path.isdir(os.path.dirname(self.log_file)):
                print("Error: Could not open logs directory, a file exists with the same name.")
                exit(1)
        else:
            os.mkdir(os.path.dirname(self.log_file))
        self.log_fd = open(self.log_file, 'w')
        self.lock.release()

    def set_update(self, target=None):
        """ Set update function to be called while the bot is logged in """
        self._userupdate = target

    def set_locale(self, locale="en_US"):
        """ Set client language. """
        self._locale = locale

    def set_debug_mode(self, debug=True):
        """ Set whether debug logging is active. """
        self._debug_mode = debug

    def set_packet_log_mode(self, debug=True):
        """ Set whether packet logging is active. """
        self._packet_log_mode = debug

    def is_on_ground(self):
        """ Returns True if the player is standing on a solid block. """
        x, y, z = self.position['x'], self.position['y'], self.position['z']
        return self._world.get(int(x), int(y), int(z), "block_data") > 0

    def login(self, host, port, username, passwd=None, run=True):
        """ Log into a server and run the bot. (unless run=False)"""
        self.username = username
        self.host, self.port = host, port
        if run:
            self.run()

    def run(self):
        """ Start the bot's main loop. """
        self.main_thread = threading.Thread(target=self._run)
        self.main_thread.start()

    def _run(self):
        self.lock = threading.Lock()
        self._init_logging()
        self._sock = socket.socket()
        self._sock.settimeout(1)
        self._connect(self.host, self.port)

        self._infolog("Logging in...")
        self._send_packet(PacketID.HANDSHAKE, bytes([PROTOCOL_VERSION]),
                          self._encode_string(self.username), self._encode_string(self.host),
                          self.port.to_bytes(4, 'big'))
        self._debuglog("Sent handshake.")
        self._infolog("Waiting for login...")
        self.is_waiting_to_spawn = True
        self._network_handler_loop()

    def _network_handler_loop(self):
        receiver_thread = None
        while True:
            try:
                self._handle_queued_packets()
                if receiver_thread is not None:
                    while receiver_thread.is_alive():
                        receiver_thread.join()
                receiver_thread = self.receive_packet()
                self.__update()
                if self._userupdate is not None:
                    self._userupdate(self)
            except KeyboardInterrupt:
                break
            except Exception as e:
                self._errorlog(e)
                # self._debuglog(list(self._world.columns.keys()))
                break

        try:
            self._sock.shutdown(socket.SHUT_RD)
            self._sock.close()
        except IOError:
            pass

        self.is_logged_in = False
        self.log_fd.close()

    def send_message(self, message):
        return self.message(message)

    def message(self, message):
        self._infolog(f"Sending message {message}")
        self.message_raw({"text": message})

    def message_raw(self, messagejson):
        self._queue_send_packet(PacketID.CHAT_MESSAGE, self._encode_string(json.dumps(messagejson)))

    def walk(self, direction, amount=1):
        if self.is_logged_in:
            dx, dz = math.cos(direction) * self.walking_speed, math.sin(direction) * self.walking_speed
            if self.is_in_water():
                pass
            self._walk_velocity = (dx, dz)
            self.walking_time = amount

    def _move_flying(self, par1, par2, par3):
        var4 = par1 ** 2 + par2 ** 2
        if var4 >= 1.0e-4:
            var4 = math.sqrt(var4)
            if var4 < 1.0:
                var4 = 1.0
            var4 = par3 / var4
            par1 *= var4
            par2 *= var4
            var5 = math.sin(self.rotation["yaw"] * math.pi / 180)
            var6 = math.cos(self.rotation["yaw"] * math.pi / 180)
            self.velocity["x"] += par1 * var6 - par2 * var5
            self.velocity["z"] += par2 * var6 + par1 * var5

    def is_in_water(self):
        block = str(
            self._world.get(int(self.position["x"]), int(self.position["y"]), int(self.position["z"]), "block_data"))
        block = Blocks.ALL[block]
        if block.iswater:
            return True
        return False

    def _push_out_of_blocks(self, x, y, z):
        x, y, z = self.position['x'], self.position['y'], self.position['z']
        block = self._world.get(int(x), int(y+1), int(z), "block_data")
        if block > 0:
            self.velocity['y'] = 0.5
        x2 = math.floor(x)
        y2 = math.floor(y)
        z2 = math.floor(z)
        x3 = x - x2
        y3 = y - y2
        z3 = z - z2
        colisionblocks = self._get_colliding_block_bounds(self.bounding_box)
        if not len(colisionblocks) and not self.get_block(x2, y2, z2).is_full_block:
            return False

    def _walk(self):
        dx, dz = self._walk_velocity
        self.velocity['x'] = dx
        self.velocity['z'] = dz

    def _update_movement(self):
        if self.is_on_ground():
            self.velocity['y'] = 0
            self.position['y'] = math.ceil(self.position['y'])
        else:
            self.velocity['y'] -= self.walking_speed*2
        self._debuglog(f"moving by {self.velocity['x']}, {self.velocity['y']}, {self.velocity['z']}")
        self.position['x'] += self.velocity['x']
        self.position['y'] += self.velocity['y']
        self.position['z'] += self.velocity['z']
        self._send_position_packet()
        self.schedule(self._update_movement, 0.05)

    def _send_position_packet(self):
        if not self.is_waiting_to_spawn:
            x, y, z = self.position['x'], self.position['y'], self.position['z']
            yaw, pitch = self.rotation["yaw"], self.rotation["pitch"]
            self._debuglog(f"Sending position {x}, {y}, {z} yaw {yaw} pitch {pitch}")
            self._queue_send_packet(PacketID.PLAYER_POSITION_AND_LOOK, self._encode_double(x), self._encode_double(y),
                                    self._encode_double(y + self.stance_offset), self._encode_double(z),
                                    self._encode_float(yaw), self._encode_float(pitch),
                                    (1 if self.is_on_ground() else 0))

    def set_event_handler(self, event, handler):
        """ Set a function to be run when an event occurs """
        self._event_handlers[event] = handler

    def __respawn(self):
        if self.health <= 0.0:
            self._entity_status = 0
            self._send_packet(PacketID.CLIENT_STATUS, 1)
            self.schedule(self.__respawn, 1)
        else:
            self.position = self.spawn_position.copy()
            self._fire_event(Event.BOT_RESPAWN)

    def __update(self):
        if self.is_logged_in:
            if self._entity_status == 2:
                self._fire_event(Event.BOT_HURT)
                if self.health <= 0.0 and not self._has_sent_respawn:
                    self._fire_event(Event.BOT_DEAD)
                    self._send_packet(PacketID.CLIENT_STATUS, 1)
                    self._has_sent_respawn = True
                    self.schedule(self.__respawn, 3)
                self._entity_status = 0

            if self.health > 0.0:
                self._has_sent_respawn = False

            if self.walking_time > 0:
                self._walk()
                self.walking_time -= 1

            i = 0
            while i < len(self.__event_queue):
                event, dt, fn = self.__event_queue[i]
                if time.time() >= dt:
                    self.__event_queue.pop(i)
                    if fn is None:
                        self._fire_event(event)
                    else:
                        fn()
                else:
                    i += 1

    def get_packet(self, i=None):
        """ Return a previously processed packet or the current packet if no index is passed. Returns None if packet
        log mode is not enabled. """
        if i is None:
            return self.__packet
        elif type(i) is int:
            return self.__oldpackets[i]
        raise ValueError("Argument must be a valid integer or None")

    def receive_packet(self):
        """ Receive a packet if a packet is available """
        receiver_thread = threading.Thread(target=self._receive_packet())
        receiver_thread.start()
        return receiver_thread

    def _receive_packet(self):
        try:
            packet_id = self._receive_int(SIZEOF_BYTE, signed=False)

            if self._packet_log_mode:
                if self.__packet is not None:
                    self.__oldpackets.append(bytes(self.__packet))
                self.__packet = [packet_id]

            self.last_packet_id = packet_id
            if packet_id == PacketID.KEEP_ALIVE:  # S<>C let the server know we're still listening
                number = self._receive(SIZEOF_INT)
                self._debuglog(f"Keepalive Received.")
                self._queue_send_packet(PacketID.KEEP_ALIVE, number)
            elif packet_id == PacketID.LOGIN_REQUEST:  # S->C server response to handshake
                self.eid = self._receive_int(SIZEOF_INT)
                self._entities[self.eid] = {"equipment": self.equipment, "position": self.position,
                                            "rotation": self.rotation, "inventory": self.inventory}
                self.level_type = self._receive_string()
                self.gamemode = self._receive_int(SIZEOF_BYTE)
                self.dimension = self._receive_int(SIZEOF_BYTE)
                self.difficulty = self._receive_int(SIZEOF_BYTE)
                self.worldheight = self._receive_int(SIZEOF_BYTE)
                self.server_max_players = self._receive_int(SIZEOF_BYTE)
                self.is_logged_in = True
                self._infolog(
                    f"Logged in. Entity ID {self.eid} Gamemode {self.gamemode} Dimension {self.dimension} Difficulty {self.difficulty} \
    Max players on server {self.server_max_players}")
                self._debuglog("Sending Client Settings...")
                self._send_packet(PacketID.CLIENT_SETTINGS, self._encode_string(self._locale), 0, 9, 3, 1)
                self.is_waiting_to_spawn = False
                self.schedule(self._update_movement, 2)
            elif packet_id == PacketID.HANDSHAKE:
                protocol_version = self._receive_int(SIZEOF_BYTE)
                server_name = self._receive_string()  # maybe?
                server_host = self._receive_string()
                server_port = self._receive_int(SIZEOF_INT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.DISCONNECT:
                reason = self._receive_string()
                try:
                    self._debuglog(f"Disconnected. Reason: {reason}")
                except UnicodeEncodeError as e:
                    self._debuglog(f"Disconnected. Reason: {self._bytes_to_str(reason)}")
                self._disconnect()
            elif packet_id == PacketID.CHAT_MESSAGE:
                message = self._receive_string()
                self._messagelog(message)
                self.last_message = message
            elif packet_id == PacketID.TIME_UPDATE:  # S->C when the world age/time updates
                self.worldage = self._receive_int(SIZEOF_LONG)
                self.timeofday = self._receive_int(SIZEOF_LONG)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.ENTITY_EQUIPMENT:  # S->C when entity equipment changes
                eid = self._receive_int(SIZEOF_ENTITYID)
                slot = self._receive_int(SIZEOF_SHORT)
                slotdata = self._receive_slot()
                if eid not in self._entities.keys():
                    self._entities[eid] = \
                        {"equipment": {}, "position": {"x": None, "y": None, "z": None},
                         "rotation": {"pitch": None, "yaw": None}, "status": 0}
                if "equipment" not in self._entities.keys():
                    self._entities[eid]["equipment"] = {}
                self._entities[eid]["equipment"][slot] = slotdata
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.SPAWN_POSITION:  # S->C when player spawnpoint changes / is set
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_INT)
                z = self._receive_int(SIZEOF_INT)
                self.spawn_position = {"x": x, "y": y, "z": z}
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.USE_ENTITY:
                user = self._receive_int(SIZEOF_INT)
                target = self._receive_int(SIZEOF_INT)
                mousebutton = self._receive_int(SIZEOF_BYTE)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.UPDATE_HEALTH:  # S->C when player health/hunger/saturation changes
                self.health = self._receive_float()
                self.food = self._receive_int(SIZEOF_SHORT)
                self.saturation = self._receive_float()
                self.can_run = self.food > 6.0
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.RESPAWN:  # S->C when player respawns
                self._debuglog("Received respawn packet")
                self.dimension = self._receive_int(SIZEOF_INT)
                self.difficulty = self._receive_int(SIZEOF_BYTE, signed=False)
                self.gamemode = self._receive_int(SIZEOF_BYTE, signed=False)
                self.worldheight = self._receive_int(SIZEOF_BYTE, signed=False)
                # self.level_type = self._receive_string()
                self._debuglog(f"Spawning in dim {self.dimension} at",
                               f"{self.spawn_position['x']}, {self.spawn_position['y']}, {self.spawn_position['z']}",
                               f"with difficulty {self.difficulty}")
                self.position = self.spawn_position.copy()
                self._queue_send_packet(PacketID.PLAYER_ON_GROUND, 1 if self.is_on_ground() else 0)
                self._queue_send_packet(PacketID.PLAYER_POSITION, self._encode_double(self.position['x']),
                                        self._encode_double(self.position['y']),
                                        self._encode_double(self.position['y'] + self.stance_offset),
                                        self._encode_double(self.position['z']), 1 if self.is_on_ground() else 0)
            elif packet_id == PacketID.PLAYER_POSITION_AND_LOOK:  # S<>C when the player moves
                self.position["x"] = self._receive_double()
                self.position["y"] = self._receive_double()
                self.stance_offset = self._receive_double() - self.position["y"]
                self.position["z"] = self._receive_double()
                self.rotation["yaw"] = self._receive_float()
                self.rotation["pitch"] = self._receive_float()
                self._on_ground = self._receive_int(SIZEOF_BYTE) > 0
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.HELD_ITEM_CHANGE:  # S<>C when held item slot changes
                self._hotbar_selection = self._receive_int(SIZEOF_SHORT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.USE_BED:  # S->C when an entity goes to sleep
                eid = self._receive_int(SIZEOF_INT)
                self._receive_int(SIZEOF_BYTE, signed=False)  # probably unused field
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_BYTE, signed=False)
                z = self._receive_int(SIZEOF_INT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.ANIMATION:  # S->C when an animation happens
                eid = self._receive_int(SIZEOF_INT)
                if eid not in self._entities.keys():
                    self._entities[eid] = {}
                self._entities[eid]["animation"] = self._receive_int(SIZEOF_BYTE, signed=False)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.SPAWN_NAMED_ENTITY:  # S->C when a named entity spawns
                eid = self._receive_int(SIZEOF_INT)
                name = self._receive_string()
                x = self._receive_fixed(SIZEOF_INT)
                y = self._receive_fixed(SIZEOF_INT)
                z = self._receive_fixed(SIZEOF_INT)
                yaw = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                pitch = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                helditem = self._receive_int(SIZEOF_SHORT, signed=False)
                metadata = self._receive_metadata()
                if eid not in self._entities.keys():
                    self._entities[eid] = {}
                self._entities[eid]["name"] = name
                self._entities[eid]["position"] = {"x": x, "y": y, "z": z}
                self._entities[eid]["rotation"] = {"pitch": pitch, "yaw": yaw}
                self._entities[eid]["helditem"] = helditem
                self._entities[eid]["metadata"] = metadata
                self._debuglog(f"Server spawned player {eid} named {name} at {x}, {y}, {z}")
            elif packet_id == PacketID.COLLECT_ITEM:  # S->C trigger item collection animation
                itemeid = self._receive_int(SIZEOF_INT)
                eid = self._receive_int(SIZEOF_INT)
                self._debuglog(f"Entity {eid} picked up item entity {itemeid}")
            elif packet_id == PacketID.SPAWN_OBJECT:  # S-C Spawn an object/vehicle
                eid = self._receive_int(SIZEOF_INT)
                _type = self._receive_int(SIZEOF_BYTE)
                x = self._receive_fixed(SIZEOF_INT)
                y = self._receive_fixed(SIZEOF_INT)
                z = self._receive_fixed(SIZEOF_INT)
                yaw = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                pitch = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                objectdata = self._receive_objectdata()
                self._debuglog(f"Server spawned object/vehicle {eid} type {_type} at {x}, {y}, {z}")
            elif packet_id == PacketID.SPAWN_MOB:  # S->C Spawn a mob
                eid = self._receive_int(SIZEOF_INT)
                _type = self._receive_int(SIZEOF_BYTE)
                x = self._receive_fixed(SIZEOF_INT)
                y = self._receive_fixed(SIZEOF_INT)
                z = self._receive_fixed(SIZEOF_INT)
                pitch = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                headpitch = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                yaw = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                vx = self._receive_int(SIZEOF_SHORT)
                vy = self._receive_int(SIZEOF_SHORT)
                vz = self._receive_int(SIZEOF_SHORT)
                metadata = self._receive_metadata()
                self._entities[eid] = {"type": _type, "position": {"x": x, "y": y, "z": z},
                                       "rotation": {"pitch": pitch, "yaw": yaw}, "headpitch": headpitch,
                                       "velocity": {"x": vx, "y": vy, "z": vz}, "metadata": metadata, "status": 0}
                self._debuglog(f"Server spawned mob {eid} type {_type} at {x}, {y}, {z}")
            elif packet_id == PacketID.SPAWN_PAINTING:  # S->C Spawn a painting
                eid = self._receive_int(SIZEOF_INT)
                title = self._receive_string()
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_INT)
                z = self._receive_int(SIZEOF_INT)
                direction = self._receive_int(SIZEOF_INT)
                self._entities[eid] = {"type": "painting", "position": {"x": x, "y": y, "z": z},
                                       "direction": direction, "title": title}
                self._debuglog(f"Server spawned painting {eid} titled {title} at {x}, {y}, {z} facing {direction}")
            elif packet_id == PacketID.SPAWN_EXPERIENCE_ORB:  # S->C Spawn an experience orb
                eid = self._receive_int(SIZEOF_INT)
                x = self._receive_fixed(SIZEOF_INT)
                y = self._receive_fixed(SIZEOF_INT)
                z = self._receive_fixed(SIZEOF_INT)
                count = self._receive_int(SIZEOF_SHORT)
                self._debuglog(f"Server spawned xp orb {eid} at {x}, {y}, {z} of value {count}")
                self._entities[eid] = {"type": "experience", "position": {"x": x, "y": y, "z": z},
                                       "count": count}
            elif packet_id == PacketID.ENTITY_VELOCITY:  # S->C Set an entity's velocity
                eid = self._receive_int(SIZEOF_INT)
                vx = self._receive_int(SIZEOF_SHORT)
                vy = self._receive_int(SIZEOF_SHORT)
                vz = self._receive_int(SIZEOF_SHORT)
                if eid in self._entities.keys():  # sanity-check if we know this entity exists yet
                    self._entities[eid]["velocity"] = {"x": vx, "y": vy, "z": vz}
                self._debuglog(f"Server set entity velocity to {vx}, {vy}, {vz}")
            elif packet_id == PacketID.DESTROY_ENTITY:  # S->C Destroy an entity
                count = self._receive_int(SIZEOF_BYTE)
                for i in range(count):
                    eid = self._receive_int(SIZEOF_INT)
                    if eid in self._entities.keys():
                        del self._entities[eid]
                self._debuglog(f"Server destroyed entity {eid}")
            elif packet_id == PacketID.ENTITY:  # S->C Initialize an entity if it hasn't been initialized yet
                eid = self._receive_int(SIZEOF_INT)
                if eid not in self._entities.keys():
                    self._entities[eid] = \
                        {"equipment": {}, "position": {"x": None, "y": None, "z": None},
                         "rotation": {"pitch": None, "yaw": None}}
                self._debuglog(f"Server initialized entity {eid}")
            elif packet_id == PacketID.ENTITY_RELATIVE_MOVE:  # S->C Sent when an entity travels less than 4 blocks
                eid = self._receive_int(SIZEOF_INT)
                dx = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
                dy = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
                dz = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
                if eid in self._entities.keys():
                    pos = self._entities[eid]["position"]
                    pos["x"] += dx
                    pos["y"] += dy
                    pos["z"] += dz
                self._debuglog(f"Server moved {eid} by {dx}, {dy}, {dz}")
            elif packet_id == PacketID.ENTITY_LOOK:  # S->C Sent when an entity rotates
                eid = self._receive_int(SIZEOF_INT)
                yaw = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                pitch = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                if eid in self._entities.keys():
                    self._entities[eid]["rotation"] = {"pitch": pitch, "yaw": yaw}
                self._debuglog(f"Server rotated {eid} to yaw {yaw} pitch {pitch}")
            elif packet_id == PacketID.ENTITY_LOOK_AND_RELATIVE_MOVE:  # S->C Sent when an entity moves less than 4 blocks and rotates
                eid = self._receive_int(SIZEOF_INT)
                dx = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
                dy = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
                dz = self._receive_fixed(SIZEOF_BYTE, fractionalbits=6)
                yaw = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                pitch = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                if eid in self._entities.keys():
                    self._entities[eid]["rotation"] = {"pitch": pitch, "yaw": yaw}
                    pos = self._entities[eid]["position"]
                    pos["x"] += dx
                    pos["y"] += dy
                    pos["z"] += dz
                self._debuglog(f"Server moved {eid} by {dx}, {dy}, {dz} and rotated to yaw {yaw} pitch {pitch}")
            elif packet_id == PacketID.ENTITY_TELEPORT:  # S->C Sent when an entity moves more than 4 blocks
                eid = self._receive_int(SIZEOF_INT)
                x = self._receive_fixed(SIZEOF_INT)
                y = self._receive_fixed(SIZEOF_INT)
                z = self._receive_fixed(SIZEOF_INT)
                yaw = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                pitch = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                self._debuglog(f"Server teleported {eid} to {x}, {y}, {z} and rotated to yaw {yaw} pitch {pitch}")
                if eid in self._entities.keys():
                    self._entities[eid]["rotation"] = {"pitch": pitch, "yaw": yaw}
                    self._entities[eid]["position"] = {"x": x, "y": y, "z": z}
            elif packet_id == PacketID.ENTITY_HEAD_LOOK:  # S->C Sent to change the direction an entity's head is facing
                eid = self._receive_int(SIZEOF_INT)
                yaw = self._receive_int(SIZEOF_BYTE, signed=False) * (math.pi / 128)
                if eid in self._entities.keys():
                    self._entities[eid]["headyaw"] = yaw
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.ENTITY_STATUS:  # S->C Set the status of an entity
                eid = self._receive_int(SIZEOF_INT)
                status = self._receive_int(SIZEOF_BYTE)
                if eid == self.eid:
                    self._entity_status = status
                elif eid in self._entities.keys():
                    self._entities[eid]["status"] = status
                self._debuglog(f"Got Packet: {hex(packet_id)} Entity {eid} Status {status}")
            elif packet_id == PacketID.ATTACH_ENTITY:  # S->C Attach an entity to another entity
                eid = self._receive_int(SIZEOF_INT)
                vid = self._receive_int(SIZEOF_INT)
                leash = self._receive_int(SIZEOF_INT)
                if eid in self._entities.keys():
                    self._entities[eid]["attachedto"] = vid
                    if leash:
                        self._entities[eid]["leashedto"] = vid
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.ENTITY_METADATA:
                eid = self._receive_int(SIZEOF_INT)
                self._debuglog(f"Received Entity Metadata packet for {eid}")
                metadata = self._receive_metadata()
                if eid == self.eid:
                    self.metadata = metadata
                if eid in self._entities.keys():
                    self._entities[eid]["metadata"] = metadata
            elif packet_id == PacketID.ENTITY_EFFECT:  # S->C Add an effect to an entity
                eid = self._receive_int(SIZEOF_INT)
                effect = self._receive_int(SIZEOF_BYTE)
                amplifier = self._receive_int(SIZEOF_BYTE)
                duration = self._receive_int(SIZEOF_SHORT)
                self._debuglog(
                    f"Received Entity Effect packet for {eid} with effect {effect} amplifier {amplifier} duration {duration}")
                if eid in self._entities.keys():
                    if "effects" not in self._entities[eid].keys():
                        self._entities[eid]["effects"] = []
                    self._entities[eid]["effects"].append(
                        {"effect": effect, "duration": duration, "amplifier": amplifier})
            elif packet_id == PacketID.REMOVE_ENTITY_EFFECT:  # S->C Remove an effect ID on an entity.
                eid = self._receive_int(SIZEOF_INT)
                effect = self._receive_int(SIZEOF_INT)
                self._debuglog(f"Received Entity Effect Remove packet for {eid} removing effect {effect}")
                if eid in self._entities.keys():
                    if "effects" in self._entities[eid].keys():
                        i = 0
                        while i < len(self._entities[eid]["effects"]):
                            if self._entities[eid]["effects"][i]["effect"] == effect:
                                self._entities[eid]["effects"].pop(i)
                            else:
                                i += 1
            elif packet_id == PacketID.SET_EXPERIENCE:  # S->C Set a player's experience levels et al
                self._experiencebar = self._receive_float()
                self._experiencelevel = self._receive_int(SIZEOF_SHORT)
                self._totalexperience = self._receive_int(SIZEOF_SHORT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.ENTITY_PROPERTIES:  # S->C Set an entity's properties. TODO: Actually make this do stuff
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
                        self._debuglog(
                            f"UUID: 0x{''.join([hex(c // 16)[2] + hex(c % 16)[2] for c in uuid])} (big-endian)")
                        self._debuglog(f"amount: {amount}")
                        self._debuglog(f"operation: {operation}")
            elif packet_id == PacketID.CHUNK_DATA:  # S->C When sending a single chunk's data
                cx = self._receive_int(SIZEOF_INT)
                cz = self._receive_int(SIZEOF_INT)
                continuous = self._receive_int(SIZEOF_BYTE)
                mask1 = self._receive_int(SIZEOF_SHORT)
                mask2 = self._receive_int(SIZEOF_SHORT)
                compresseddatalen = self._receive(SIZEOF_INT)
                compresseddata = self._receive(int.from_bytes(compresseddatalen, 'big', signed=True))
                data = zlib.decompress(compresseddata)
                key = (cx, cz)
                if key in self._world.columns:
                    column = self._world.columns[key]
                else:
                    column = ChunkColumn()
                    self._world.columns[key] = column
                column.unpack(data, mask1, mask2, skylight=True)  # Unpack the chunk column data
                self._debuglog(f"Loaded chunk packet for chunk: ({cx}, {cz})")
            elif packet_id == PacketID.MULTI_BLOCK_CHANGE:  # S->C When multiple blocks update.
                cx = self._receive_int(SIZEOF_INT)
                cz = self._receive_int(SIZEOF_INT)
                recordcount = self._receive_int(SIZEOF_SHORT)
                datasize = self._receive_int(SIZEOF_INT)
                key = (cx, cz)
                for i in range(recordcount):
                    record = self._receive_int(4)
                    metadata = record & 0x0000000F
                    blockid = (record & 0x0000FFF0) // 0x00000010
                    y = (record & 0x00FF0000) // 0x00010000
                    z = (record & 0x0F000000) // 0x01000000
                    x = (record & 0xF0000000) // 0x10000000
                    self._update_block(cx, cz, x, y, z, blockid, metadata)
            elif packet_id == PacketID.BLOCK_CHANGE:  # S->C When a block updates.
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_BYTE, signed=False)
                z = self._receive_int(SIZEOF_INT)
                blocktype = self._receive_int(SIZEOF_SHORT)
                metadata = self._receive_int(SIZEOF_BYTE, signed=False)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
                self._update_block(x // 16, z // 16, x & 15, y, z & 15, blocktype & 0xFF, metadata)
            elif packet_id == PacketID.BLOCK_ACTION:
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_SHORT)
                z = self._receive_int(SIZEOF_INT)
                b1 = self._receive_int(SIZEOF_BYTE)
                b2 = self._receive_int(SIZEOF_BYTE)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.BLOCK_BREAK_ANIMATION:
                eid = self._receive_int(SIZEOF_INT)
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_SHORT)
                z = self._receive_int(SIZEOF_INT)
                destroystage = self._receive_int(SIZEOF_BYTE)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.MAP_CHUNK_BULK:  # S->C When sending several chunks
                chunkcount = self._receive(SIZEOF_SHORT)
                datalen = self._receive(SIZEOF_INT)
                skylightsent = self._receive(SIZEOF_BYTE)
                data = list(self._receive(int.from_bytes(datalen, 'big', signed=True)))
                for i in range(int.from_bytes(chunkcount, 'big', signed=True)):
                    data.extend(self._receive(SIZEOF_INT * 2 + SIZEOF_SHORT * 2))
                self._world.unpack(chunkcount + datalen + skylightsent + bytes(data))
                self._debuglog("Loaded bulk chunk packet.")
            elif packet_id == PacketID.EXPLOSION:
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
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.SOUND_OR_PARTICLE_EFFECT:
                effectid = self._receive_int(SIZEOF_INT)
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_BYTE, signed=False)
                z = self._receive_int(SIZEOF_INT)
                data = self._receive_int(SIZEOF_INT)
                disablerelativevolume = self._receive_int(SIZEOF_BYTE)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.NAMED_SOUND_EFFECT:
                soundname = self._receive_string()
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_INT)
                z = self._receive_int(SIZEOF_INT)
                volume = self._receive_float()
                pitch = self._receive_int(SIZEOF_BYTE)  # 63 = 100%
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.PARTICLE:
                particlename = self._receive_string()
                x = self._receive_float()
                y = self._receive_float()
                z = self._receive_float()
                ox = self._receive_float()
                oy = self._receive_float()
                oz = self._receive_float()
                speed = self._receive_float()
                number = self._receive_int(SIZEOF_INT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.CHANGE_GAME_STATE:
                reason = self._receive_int(SIZEOF_BYTE)
                gamemode = self._receive_int(SIZEOF_BYTE)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
                if reason == 1:
                    self._debuglog("It is now raining")
                    self._is_raining = True
                elif reason == 2:
                    self._debuglog("It is no longer raining")
                    self._is_raining = False
                elif reason == 3:
                    self._debuglog("Gamemode has been updated to", gamemode)
                    self.gamemode = gamemode
            elif packet_id == PacketID.SPAWN_GLOBAL_ENTITY:
                entityid = self._receive_int(SIZEOF_INT)
                entitytype = self._receive_int(SIZEOF_BYTE)
                x = self._receive_fixed(SIZEOF_INT)
                y = self._receive_fixed(SIZEOF_INT)
                z = self._receive_fixed(SIZEOF_INT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.OPEN_WINDOW:
                windowid = self._receive_int(SIZEOF_BYTE, signed=False)
                windowtype = self._receive_int(SIZEOF_BYTE, signed=False)
                if windowtype not in (73,):
                    windowtitle = self._receive_string()
                    numberofslots = self._receive_int(SIZEOF_BYTE)
                else:
                    windowtitle = ""
                    numberofslots = 0
                useprovidedwindowtitle = self._receive_int(SIZEOF_BYTE)
                self._debuglog(
                    f"Opening Window ID {windowid} type {windowtype} title \"{windowtitle}\" slots {numberofslots} using provided title? {useprovidedwindowtitle}")
                if windowtype == 11:  # AnimalChest
                    entityid = self._receive_int(SIZEOF_INT)
            elif packet_id == PacketID.CLOSE_WINDOW:
                windowid = self._receive_int(SIZEOF_BYTE, signed=False)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.SET_SLOT:
                windowid = self._receive_int(SIZEOF_BYTE, signed=False)
                slot = self._receive_int(SIZEOF_SHORT)
                slotdata = self._receive_slot()
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.SET_WINDOW_ITEMS:
                windowid = self._receive_int(SIZEOF_BYTE, signed=False)
                count = self._receive_int(SIZEOF_SHORT)
                slots = []
                for i in range(count):
                    slots.append(self._receive_slot())
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.UPDATE_WINDOW_PROPERTY:
                windowid = self._receive_int(SIZEOF_BYTE, signed=False)
                prop = self._receive_int(SIZEOF_SHORT)
                value = self._receive_int(SIZEOF_SHORT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.CONFIRM_TRANSACTION:
                windowid = self._receive_int(SIZEOF_BYTE, signed=False)
                actionnumber = self._receive_int(SIZEOF_SHORT)
                accepted = self._receive_int(SIZEOF_BYTE)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.CREATIVE_INVENTORY_ACTION:
                slot = self._receive_int(SIZEOF_SHORT)
                item = self._receive_slot()
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.UPDATE_SIGN:
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_SHORT)
                z = self._receive_int(SIZEOF_INT)
                line1 = self._receive_string()
                line2 = self._receive_string()
                line3 = self._receive_string()
                line4 = self._receive_string()
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.ITEM_DATA:
                itemtype = self._receive_int(SIZEOF_SHORT)
                itemid = self._receive_int(SIZEOF_SHORT)
                datalen = self._receive_int(SIZEOF_SHORT)
                data = self._receive(datalen)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.UPDATE_TILE_ENTITY:
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_SHORT)
                z = self._receive_int(SIZEOF_INT)
                action = self._receive_int(SIZEOF_BYTE)
                datalen = self._receive_int(SIZEOF_SHORT)
                if datalen > 0:
                    data = self._receive(datalen)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.TILE_EDITOR_OPEN:
                tileentityid = self._receive_int(SIZEOF_BYTE)
                x = self._receive_int(SIZEOF_INT)
                y = self._receive_int(SIZEOF_INT)
                z = self._receive_int(SIZEOF_INT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.INCREMENT_STATISTIC:
                statid = self._receive_int(SIZEOF_INT)
                amount = self._receive_int(SIZEOF_INT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.PLAYER_LIST_ITEM:
                name = self._receive_string()
                online = self._receive_int(SIZEOF_BYTE)
                ping = self._receive_int(SIZEOF_SHORT)
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.PLAYER_ABILITIES:
                flags = self._receive_int(SIZEOF_BYTE)
                self.in_godmode = (flags & 8) != 0
                self.can_fly = (flags & 4) != 0
                self.is_flying = (flags & 2) != 0
                self.in_creative_mode = (flags & 1) != 0
                self.flying_speed = self._receive_float()
                self.walking_speed = self._receive_float()
                self._debuglog(f"Got Player Abilities: walking speed: {self.walking_speed} flying speed: {self.flying_speed}"
                               f"can fly: {self.can_fly} is flying {self.is_flying}"
                               f"is in creative mode: {self.in_creative_mode} god mode: {self.in_godmode}")
            elif packet_id == PacketID.TAB_COMPLETE:
                self.tab_completed_string = self._receive_string()
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.SCOREBOARD_OBJECTIVE:
                objectivename = self._receive_string()
                objectivevalue = self._receive_string()
                createremove = self._receive_int(SIZEOF_BYTE)  # 0 to create, 1 to remove, 2 to update display text
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.UPDATE_SCORE:
                itemname = self._receive_string()
                updateremove = self._receive_int(SIZEOF_BYTE)  # 0 to create/update, 1 to remove
                if updateremove != 1:
                    scorename = self._receive_string()
                    value = self._receive_int()
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.DISPLAY_SCOREBOARD:
                position = self._receive_int(SIZEOF_BYTE)  # 0 = list, 1 = sidebar, 2 = belowName
                scorename = self._receive_string()
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.TEAMS:
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
                self._debuglog(f"Got Packet: {hex(packet_id)}")
            elif packet_id == PacketID.PLUGIN_MESSAGE:
                channel = self._receive_string()
                datalen = self._receive_int(SIZEOF_SHORT)
                if datalen > 0:
                    data = self._receive(datalen)
                else:
                    data = ""
                if channel == "MC|Brand":
                    self.server_brand = data
                self._infolog("Plugin Message Received:", channel, data)
            elif packet_id == PacketID.ENCRYPTION_KEY_REQUEST:  # S->C Server sends serverid, pubkey, and verifytoken
                self._serverid = self._receive_string()
                self._serverpubkeylen = self._receive_int(SIZEOF_SHORT)
                self._serverpubkey = self._receive(self._serverpubkeylen)
                self._verifytokenlen = self._receive_int(SIZEOF_SHORT)
                self._verifytoken = self._receive(self._verifytokenlen)

                #            self._serverpubkey_object = RSA.import_key(self._serverpubkey)

                #            sharedsecret = os.urandom(16)
                #            cipher = PKCS1_v1_5.new(self._serverpubkey_object)
                #            cipheredsecret = cipher.encrypt(sharedsecret)
                #            cipheredverifytoken = cipher.encrypt(self._verifytoken)

                #            self._decrypt_cipher = AES.new(sharedsecret, AES.MODE_CFB, sharedsecret)
                #            self._encrypt_cipher = AES.new(sharedsecret, AES.MODE_CFB, sharedsecret)

                #            self._send_packet(PacketID.ENCRYPTION_KEY_RESPONSE, len(cipheredsecret).to_bytes(SIZEOF_SHORT, 'big'),
                #                              cipheredsecret, len(cipheredverifytoken).to_bytes(SIZEOF_SHORT, 'big'),
                #                              cipheredverifytoken)

                self._debuglog("Sending Client Statuses...")
                self._queue_send_packet(PacketID.CLIENT_STATUS, 0)  # tell the server we're ready to spawn

            elif packet_id == PacketID.ENCRYPTION_KEY_RESPONSE:
                string1len = self._receive_int(SIZEOF_SHORT)
                if string1len > 0:
                    string1 = self._receive(string1len)
                    self._debuglog("Got shared secret:", string1)
                string2len = self._receive_int(SIZEOF_SHORT)
                if string2len > 0:
                    string2 = self._receive(string2len)
                    self._debuglog("Got verify token:", string2)
                self._outbound_encryption_enabled = True
                self._inbound_encryption_enabled = True
            else:
                self._debuglog(f"Got Unknown Packet: {hex(packet_id)}")

            self._fire_event(packet_id)
        except RuntimeError:
            pass
        except OSError:
            pass

    def _fire_event(self, event):
        if event in self._event_handlers.keys():
            self._debuglog("Firing Event Handler for Event", event)
            return self._event_handlers[event](self)
        return None

    def schedule(self, function, dt):
        self.__event_queue.append((Event.GENERAL_EVENT, time.time() + dt, function))

    def schedule_event(self, event, dt):
        self.__event_queue.append((event, time.time() + dt, None))

    def _update_block(self, cx, cz, x, y, z, blockid, metadata):
        if x in range(16) and z in range(16):
            # self._debuglog(f"[_update_block] updating block {x}, {y}, {z} in chunk {cx}, {cz} to {blockid}:{metadata}")
            key = (cx, cz)
            if key not in self._world.columns.keys():
                self._world.columns[key] = ChunkColumn()
            column = self._world.columns[key]
            if column is None:
                column = self._world.columns[key] = ChunkColumn()
            chunk = column.chunks[y // 16]
            if chunk is None:
                chunk = column.chunks[y // 16] = Chunk()
            chunk['block_data'].put(x, y & 0xF, z, blockid)
            chunk['block_meta'].put(x, y & 0xF, z, metadata)
        else:
            self._debuglog(f"[_update_block] failed: ({x}, {y}, {z}) is outside the allowed range. (16, 256, 16)")

    def connect(self, addr=None, port=MC_DEFAULT_PORT):
        if addr is None:
            if self.is_running:
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

    def disconnect(self):
        if self.is_logged_in:
            self._disconnect()

    def _connect(self, addr, port=MC_DEFAULT_PORT):
        self._sock.connect((addr, port))
        self.is_running = True

    def _disconnect(self):
        try:
            self._queue_send_packet(PacketID.DISCONNECT, 0, 0)
        except OSError:
            pass


        self.is_logged_in = False
        self.is_running = False

        # wait for the packet handling thread to complete
        time.sleep(0.25)

    def _errorlog(self, *args):
        self.__logwrite("[E]", " ".join([str(arg) for arg in args]))

    def _warning(self, *args):
        self.__logwrite("[W]", " ".join([str(arg) for arg in args]))

    def _infolog(self, *args):
        self.__logwrite("[I]", " ".join([str(arg) for arg in args]))

    def _debuglog(self, *args):
        if self._debug_mode:
            self.__logwrite("[D]", " ".join([str(arg) for arg in args]))

    def _messagelog(self, *args):
        self.lock.acquire(blocking=True)
        self.__logwrite("[M]", " ".join([str(arg) for arg in args]))
        self.lock.release()

    def __logwrite(self, *args):
        s = " ".join([arg for arg in args])
        print(s)
        self.log_fd.write(s)
        self.log_fd.write("\n")

    def read(self, amt=1):
        return self._receive(amt)

    def _receive_metadata(self, data=None):
        metadata = {}
        while True:
            item = self._receive_int(SIZEOF_BYTE, signed=False, data=data)
            if item == 0x7F:
                return metadata
            key, _type = item & 0x1F, item // 2 ** 5
            if _type in ENTITY_METADATA_VALUE_TYPE_READERS.keys():
                reader = ENTITY_METADATA_VALUE_TYPE_READERS[_type]
                value = reader(self, data)
                metadata[key] = {"value": value, "type": _type}
                self._debuglog(f"Read entity metadata type: {_type} with key {key} value {value}")
            else:
                # self._errorlog(f"Received invalid entity metadata key {key} type {_type}")
                raise ValueError(f"Invalid entity metadata received: key {key} type {_type} ({hex(item)})")

    def _receive_slot(self, data=None):
        itemid = self._receive_int(SIZEOF_SHORT, data=data)
        self._debuglog("receiving slot...")
        self._debuglog(f"item id: {itemid}")
        if itemid >= 0:
            itemcount = self._receive_int(SIZEOF_BYTE, data=data)
            itemdamage = self._receive_int(SIZEOF_SHORT, data=data)
            nbtsize = self._receive_int(SIZEOF_SHORT, data=data)
            self._debuglog(f"count: {itemcount} damage: {itemdamage} nbt bytes: {nbtsize}")
            if nbtsize <= 0:
                return {"id": itemid, "count": itemcount, "nbt": None}
            data = gzip.decompress(self._receive(nbtsize, data=data))
            # self._debuglog("Decompressed NBT data:", data.hex())
            nbt = NBT(data)
            self._debuglog("NBT:", nbt)
            return {"id": itemid, "count": itemcount, "nbt": nbt}
        else:
            return {"id": -1, "count": -1, "nbt": None}

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
        num = self._receive_int(SIZEOF_SHORT, signed=True, data=data)
        if num > 0:
            if data is None:
                return self._bytes_to_str(self._receive(num * 2, data=data))
            else:
                return self._bytes_to_str(data[:num * 2])
        return ""

    def _receive_objectdata(self, data=None):
        intfield = self._receive_int(SIZEOF_INT, data=data)
        if intfield == 0:
            return {"intfield": intfield}
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
                break
            chunks.append(data)
        return self._decipher(b''.join(data))

    def __receive(self, amt, data):
        if self.is_running:
            if data is None:
                bytes_recd = 0
                chunks = []
                while bytes_recd < amt:
                    chunk = self._sock.recv(min(amt - bytes_recd, 2048))
                    if chunk == b'':
                        # self._errorlog("Socket Connection Broken")
                        raise RuntimeError("Socket Connection Broken")
                    chunks.append(chunk)
                    bytes_recd = bytes_recd + len(chunk)
                return self._decipher(b''.join(chunks))
            else:
                o = []
                for i in range(amt):
                    o.append(data.pop(0))
                return self._decipher(bytes(o))
        else:
            # self._errorlog("Socket Connection Broken")
            raise RuntimeError("Socket Connection Broken")

    def _send(self, *args):
        data = b''.join([data for data in args])
        if self._sock.sendall(self._encipher(data)) is not None:
            self._errorlog("Socket Connection Broken")
            raise RuntimeError("socket connection broken")

    def _queue_send_packet(self, packetid, *args):
        self.__packetqueue.append((packetid, [arg for arg in args]))

    def _handle_queued_packets(self):
        i = 0
        while i < len(self.__packetqueue):
            packetid, args = self.__packetqueue[i]
            try:
                self._send_packet(packetid, *args)
                self.__packetqueue.pop(i)
                continue
            except TimeoutError:
                pass
            except OSError:
                pass
            i += 1

    def _send_packet(self, packetid, *args):
        o = [packetid]
        for arg in args:
            if type(arg) is int:
                o.extend(arg.to_bytes(1, 'big', signed=False))
            elif type(arg) is bytes:
                o.extend(list(arg))
            elif type(arg) is str:
                o.extend(self._str_to_bytes(arg))
        self._debuglog("Sending packet:", bytes(o).hex())
        self._send(bytes(o))

    def _encode_string(self, data):
        return len(data).to_bytes(2, 'big', signed=True) + self._str_to_bytes(data)

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
            c = data[i + 1] + data[i] * 256
            if c in range(128):
                o.append(chr(c))
            else:
                o.append(f"\\{hex(c)[1:]}")
            i += 2
        return "".join(o)

    def _decode_float(self, data):
        # self._debuglog(f"Unpacking float from 0x{''.join([hex(c//16)[2]+hex(c%16)[2] for c in data])} (big-endian)")
        try:
            n = struct.unpack('>f', data)[0]
            # self._debuglog(f"Unpacked float {n}")
            return n
        except struct.error:
            self._warning(
                f"[_decode_float] Failed to unpack float from data: 0x{''.join([hex(c // 16)[2] + hex(c % 16)[2] for c in data])} (big-endian)")

    def _decode_double(self, data):
        # self._debuglog(f"[_decode_double] Unpacking double from 0x{''.join([hex(c//16)[2]+hex(c%16)[2] for c in data])} (big-endian)")
        try:
            n = struct.unpack('>d', data)[0]
            # self._debuglog(f"[_decode_double] Unpacked double {n}")
            return n
        except struct.error:
            self._warning(
                f"[_decode_double] Failed to unpack double from data: 0x{''.join([hex(c // 16)[2] + hex(c % 16)[2] for c in data])} (big-endian)")

    def _encode_float(self, data):
        # self._debuglog(f"[_encode_float] Packing float {data}")
        try:
            n = struct.pack('>f', data)
            return n
        except struct.error:
            self._warning(f"[_encode_float] Failed to encode float {data}")

    def _encode_double(self, data):
        # self._debuglog(f"[_encode_double] Packing double {data}")
        try:
            n = struct.pack('>d', data)
            return n
        except struct.error:
            self._warning(f"[_encode_double] Failed to encode double {data}")

    def _encipher(self, data):
        if self._outbound_encryption_enabled:
            return self._encrypt_cipher.encrypt(data)
        return data

    def _decipher(self, data):
        if self._inbound_encryption_enabled:
            return self._decrypt_cipher.decrypt(data)
        return data


if __name__ == '__main__':
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
                if i + 1 < len(sys.argv):
                    address = sys.argv[i + 1]
            elif sys.argv[i] in ("-p", "--port"):
                if i + 1 < len(sys.argv):
                    port = sys.argv[i + 1]
            elif sys.argv[i] in ("-u", "--user"):
                if i + 1 < len(sys.argv):
                    username = sys.argv[i + 1]
            elif sys.argv[i] in ("-w", "--passwd"):
                if i + 1 < len(sys.argv):
                    passwd = sys.argv[i + 1]

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
        # Connect to the server, log in and run the bot
        client.login(address, port, username, passwd)
