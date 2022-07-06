"""

This module is taken and edited from https://github.com/barneygale/smpmap.

This module intends to give an overview of how chunks are packed and unpacked
in the minecraft smp protocol. It provides a simple world manager that makes
use of the smp packet format internally.

Last updated for 1.4.6

"""

import array
import struct
import zlib


# try:
# from cStringIO import StringIO
# except ImportError:
# from StringIO import StringIO

class Buffer:
    def __init__(self, data=[]):
        if type(data) is bytes:
            data = list(data)
        self._data = data
        self._i = 0

    def read(self, amt=1):
        rv = self._data[self._i:self._i + amt]
        self._i += amt
        return bytes(rv)


class BiomeData:
    """ A 16x16 array stored in each ChunkColumn. """
    data = None

    def fill(self):
        if self.data is None:
            self.data = [0] * 256

    def unpack(self, buff):
        if type(buff) is not Buffer:
            buff = Buffer(buff)
        self.data = list(buff.read(256))

    def pack(self):
        return self.data.tostring()

    def get(self, x, z):
        self.fill()
        return self.data[x + z * 16]

    def put(self, x, z, d):
        self.fill()
        self.data[x + z * 16] = d


class ChunkData:
    """ A 16x16x16 array for storing block IDs. """
    length = 16 * 16 * 16
    data = None

    def fill(self):
        if self.data is None:
            self.data = [0] * self.length

    def unpack(self, buff):
        if type(buff) is not Buffer:
            buff = Buffer(buff)
        self.data = list(buff.read(self.length))

    def pack(self):
        self.fill()
        return self.data.tostring()

    def get(self, x, y, z):
        self.fill()
        if x in range(16) and y in range(16) and z in range(16):
            return self.data[x + ((y * 16) + z) * 16]
        else:
            raise IndexError(f"Chunk subsection position {x},{y},{z} is out of bounds")

    def put(self, x, y, z, data):
        self.fill()
        if x in range(16) and y in range(16) and z in range(16):
            self.data[x + ((y * 16) + z) * 16] = data
        else:
            raise IndexError(f"Chunk subsection position {x},{y},{z} is out of bounds")


class ChunkDataNibble(ChunkData):
    """ A 16x16x8 array for storing metadata, light or add. Each array element
	contains two 4-bit elements. """
    length = 16 * 16 * 8

    def get(self, x, y, z):
        self.fill()
        i = x + ((y * 16) + z) * 16
        i, r = divmod(i, 2)

        try:
            if r == 0:
                return self.data[i] // 2 ** 4
            else:
                return self.data[i] & 0x0F
        except IndexError:
            raise IndexError(f"Chunk subsection position {x * 2},{y},{z} is out of bounds")

    def put(self, x, y, z, data):
        self.fill()
        i = x + ((y * 16) + z) * 16
        i, r = divmod(i, 2)

        try:
            if r == 0:
                self.data[i] = (self.data[i] & 0x0F) | ((data & 0x0F) * 2 ** 4)
            else:
                self.data[i] = (self.data[i] & 0xF0) | (data & 0x0F)
        except IndexError:
            raise IndexError(f"Chunk subsection position {x * 2},{y},{z} is out of bounds")


class Chunk(dict):
    """ Collates the various data arrays """

    def __init__(self):
        self['block_data'] = ChunkData()
        self['block_meta'] = ChunkDataNibble()
        self['block_add'] = ChunkDataNibble()
        self['light_block'] = ChunkDataNibble()
        self['light_sky'] = ChunkDataNibble()


class ChunkColumn:
    """ Initialised chunks are a Chunk, otherwise None. """

    def __init__(self):
        self.chunks = [None] * 16
        self.biome = BiomeData()

    def unpack(self, buff, mask1, mask2, skylight=True):
        if type(buff) is not Buffer:
            buff = Buffer(buff)
        # In the protocol, each section is packed sequentially (i.e. attributes
        # pertaining to the same chunk are *not* grouped)
        self.unpack_section(buff, 'block_data', mask1)
        self.unpack_section(buff, 'block_meta', mask1)
        self.unpack_section(buff, 'light_block', mask1)
        if skylight:
            self.unpack_section(buff, 'light_sky', mask1)
        self.unpack_section(buff, 'block_add', mask2)
        self.biome.unpack(buff)

    def unpack_section(self, buff, section, mask):
        # Iterate over the bitmask
        if type(buff) is not Buffer:
            buff = Buffer(buff)
        for i in range(16):
            if mask & (2 ** i):
                if self.chunks[i] == None:
                    self.chunks[i] = Chunk()
                self.chunks[i][section].unpack(buff)


class World:
    """ A bunch of ChunkColumns. """

    def __init__(self):
        self.columns = {}  # chunk columns are address by a tuple (x, z)

    def unpack_raw(self, buff, ty):
        return struct.unpack('>' + ty, buff.read(struct.calcsize(ty)))

    def unpack(self, data):
        buff = Buffer(data)
        chunk_count = self.unpack_raw(buff, 'h')[0]  # short
        data_len = self.unpack_raw(buff, 'i')[0]  # int
        light_data = self.unpack_raw(buff, '?')[0]  # bool

        # Read compressed data
        data = buff.read(data_len)
        try:
            data = zlib.decompress(data)
        except:
            return
        # data = StringIO(data)

        for i in range(chunk_count):
            # Read chunk metadata
            chunk_x, chunk_z, mask1, mask2 = self.unpack_raw(buff, 'iihh')

            # Grab the relevant column
            key = (chunk_x, chunk_z)
            if key in self.columns:
                column = self.columns[key]
            else:
                column = ChunkColumn()
                self.columns[key] = column

            # Unpack the chunk column data!
            column.unpack(data, mask1, mask2, light_data)

    def get(self, x, y, z, key):
        x, rx = divmod(x, 16)
        y, ry = divmod(y, 16)
        z, rz = divmod(z, 16)

        if not (x, z) in self.columns:
            return 0
        column = self.columns[(x, z)]

        chunk = column.chunks[y]
        if chunk is None:
            return 0

        return chunk[key].get(rx, ry, rz)

    def put(self, x, y, z, key, data):
        x, rx = divmod(x, 16)
        y, ry = divmod(y, 16)
        z, rz = divmod(z, 16)

        if (x, z) in self.columns:
            column = self.columns[(x, z)]
        else:
            column = ChunkColumn()
            self.columns[(x, z)] = column

        chunk = column.chunks[y]
        if chunk is None:
            chunk = Chunk()
            column.chunks[y] = chunk

        chunk[key].put(rx, ry, rz, data)

    def get_biome(self, x, z):
        x, rx = divmod(x, 16)
        z, rz = divmod(z, 16)

        if (x, z) not in self.columns:
            return 0

        return self.columns[(x, z)].biome.get(rx, rz)

    def set_biome(self, x, z, data):
        x, rx = divmod(x, 16)
        z, rz = divmod(z, 16)

        if (x, z) in self.columns:
            column = self.columns[(x, z)]
        else:
            column = ChunkColumn()
            self.columns[(x, z)] = column

        return column.biome.put(rx, rz, data)


if __name__ == '__main__':
    world = World()
    with open('packet0x38.bin', 'rb') as f:
        # Strip off the packet ID
        assert f.read(1) == '\x38'

        # Unpack the rest of the packet
        world.unpack(f)
# print "Got %d columns" % len(world.columns)
