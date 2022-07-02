
class Event:
	KEEPALIVE        = 0x00
	LOGINREQUEST     = 0x01
	HANDSHAKE        = 0x02
	CHATMESSAGE      = 0x03
	TIMEUPDATE       = 0x04
	ENTITYEQUIPMENT  = 0x05
	SPAWNPOSITION    = 0x06
	USEENTITY        = 0x07
	UPDATEHEALTH     = 0x08
	RESPAWN          = 0x09
	PLAYER           = 0x0A
	PLAYERPOS        = 0x0B
	PLAYERLOOK       = 0x0C
	PLAYERPOSANDLOOK = 0x0D
	PLAYERDIGGING    = 0x0E
	PLAYERPLACEBLOCK = 0x0F
	HELDITEMCHANGE   = 0x10
	USEBED           = 0x11
	ANIMATION        = 0x12
	ENTITYACTION     = 0x13
	SPAWNNAMEDENTITY = 0x14
	COLLECTITEM      = 0x16
	SPAWNOBJECT      = 0x17
	SPAWNMOB         = 0x18
	SPAWNPAINTING    = 0x19
	SPAWNEXPORB      = 0x1A
	STEERVEHICLE     = 0x1B
	ENTITYVELOCITY   = 0x1C
	DESTROYENTITY    = 0x1D
	ENTITY           = 0x1E
	ENTITYRELMOVE    = 0x1F
	ENTITYLOOK       = 0x20
	ENTITYLOOKANDRELMOVE=0x21
	ENTITYTELEPORT   = 0x22
	ENTITYHEADLOOK   = 0x23
	ENTITYSTATUS     = 0x26
	ATTACHENTITY     = 0x27
	ENTITYMETADATA   = 0x28
	ENTITYEFFECT     = 0x29
	REMOVEENTITYEFFECT= 0x2A
	SETEXPERIENCE    = 0x2B
	ENTITYPROPERTIES = 0x2C
	CHUNKDATA        = 0x33
	MULTIBLOCKCHANGE = 0x34
	BLOCKCHANGE      = 0x35
	BLOCKACTION      = 0x36
	BLOCKBREAKANIMATION=0x37
	MAPCHUNKBULK     = 0x38
	EXPLOSION        = 0x3C
	SOUNDORPARTICLEEFFECT=0x3D
	NAMEDSOUNDEFFECT = 0x3E
	PARTICLE         = 0x3F
	CHANGEGAMESTATE  = 0x46
	SPAWNGLOBALENTITY= 0x47
	OPENWINDOW       = 0x64
	CLOSEWINDOW      = 0x65
	CLICKWINDOW      = 0x66
	SETSLOT          = 0x67
	SETWINDOWITEMS   = 0x68
	UPDATEWINDOWPROPERTY=0x69
	CONFIRMTRANSACTION=0x6A
	CREATIVEINVENTORYACTION=0x6B
	ENCHANTITEM      = 0x6C
	UPDATESIGN       = 0x82
	ITEMDATA         = 0x83
	UPDATETILEENTITY = 0x84
	TILEEDITOROPEN   = 0x85
	INCREMENTSTATISTIC=0xC8
	PLAYERLISTITEM   = 0xC9
	PLAYERABILITIES  = 0xCA
	TABCOMPLETE      = 0xCB
	CLIENTSETTINGS   = 0xCC
	CLIENTSTATUSES   = 0xCD
	SCOREBOARDOBJECTIVE=0xCE
	UPDATESCORE      = 0xCF
	DISPLAYSCOREBOARD= 0xD0
	TEAMS            = 0xD1
	PLUGINMESSAGE    = 0xFA
	ENCRYPTIONKEYRESPONSE=0xFC
	ENCRYPTIONKEYREQUEST=0xFD
	SERVERLISTPING   = 0xFE
	DISCONNECT       = 0xFF

	BOTATTACKED      = 0x102
	BOTDEAD          = 0x103
