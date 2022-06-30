

class EntityMetadata:
	BYTE         = 0x00
	VARINT       = 0x01
	FLOAT        = 0x02
	STRING       = 0x03
	CHAT         = 0x04
	OPTCHAT      = 0x05
	SLOT         = 0x06
	BOOLEAN      = 0x07
	ROTATION     = 0x08
	POSITION     = 0x09
	OPTPOSITION  = 0x0A
	DIRECTION    = 0x0B
	OPTUUID      = 0x0C
	OPTBLOCKID   = 0x0D
	NBT          = 0x0E
	PARTICLE     = 0x0F
	VILLAGERDATA = 0x10
	OPTVARINT    = 0x11
	POSE         = 0x12
	CATVARIANT   = 0x13
	FROGVARIANT  = 0x14
	PAINTINGVARIANT=0x15

	F_FLAGS            = 0x00
	F_AIRTICKS         = 0x01
	F_CUSTOMNAME       = 0x02
	F_CUSTOMNAMEVISIBLE= 0x03
	F_ISSILENT         = 0x04
	F_HASNOGRAVITY     = 0x05
	F_POSE             = 0x06
	F_FROZENTICKS      = 0x07

	def __init__(self, data=None):
		self._data = [None]*32
		if data is not None:
			if hasattr(data, "read"):
				while True:
					c = data.read()
					if c == F_FLAGS
