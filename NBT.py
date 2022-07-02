
TAG_End         = 0x00
TAG_Byte        = 0x01
TAG_Short       = 0x02
TAG_Int         = 0x03
TAG_Long        = 0x04
TAG_Float       = 0x05
TAG_Double      = 0x06
TAG_Byte_Array  = 0x07
TAG_String      = 0x08
TAG_List        = 0x09
TAG_Compound    = 0x0A
TAG_Int_Array   = 0x0B
TAG_Long_Array  = 0x0C

# 0a0003746167090004656e63680a000000010200036c766c0001020002696400300000
# TAG_Compound tag
#   TAG_List ench, TAG_Compund
#       TAG_Short lvl: 0x01
#       TAG_Short id: 0x30
#     TAG_End
# TAG_End

class NBT:
	def __init__(self, data=None):
		if type(data) is bytes or type(data) is tuple:
			self._data = self._decode(list(data))
		elif type(data) is list:
			self._data = self._decode(data.copy())
		elif type(data) is NBT:
			self._data = data.copy()
		elif hasattr(data, "read"):
			self._data = self._decode(data)
		else:
			self._data = {}

	def __bytes__(self):
		return bytes(self._encode(self._data))

	def _encode(self, k, v):
		return [self._encode_type(v)] + self._encode_key(k) + self._encode_value(v)

	def _decode(self, data=None):
		self._finished_reading = False
		return self.__decode(data)

	def __decode(self, data):
		_data = {}
		while self.__decode_value(data, _data):
			if self._finished_reading:
				break
		return _data

	def __decode_value(self, data, _data):
		c = self._read_byte(data)
		if c == TAG_End or self._finished_reading:
			return False
		key, value = self.__decode_value_type(data, c)
		_data[key] = value
		return True

	def __decode_value_type(self, data, c):
		key = self._read_key(data)
		if c == TAG_Byte:
			return key, self._read_byte(data)
		elif c == TAG_Short:
			return key, int.from_bytes(self._read_byte(data, 2), 'big', signed=True)
		elif c == TAG_Int:
			return key, int.from_bytes(self._read_byte(data, 4), 'big', signed=True)
		elif c == TAG_Long:
			return key, int.from_bytes(self._read_byte(data, 8), 'big', signed=True)
		elif c == TAG_Float:
			return key, float.fromhex(hex(bytes(self._read_byte(data, 4))))
		elif c == TAG_Double:
			return key, float.fromhex(hex(bytes(self._read_byte(data, 8))))
		elif c == TAG_Byte_Array:
			amt = int.from_bytes(self._read_byte(data, 4), 'big', signed=True)
			return key, bytearray(self._read_byte(data, amt))
		elif c == TAG_Int_Array:
			amt = int.from_bytes(self._read_byte(data, 4), 'big', signed=True)
			o = []
			for i in range(amt):
				o.append(int.from_bytes(self._read_byte(data, 4), 'big', signed=True))
			return key, o
		elif c == TAG_Long_Array:
			amt = int.from_bytes(self._read_byte(data, 4), 'big', signed=True)
			o = []
			for i in range(amt):
				o.append(int.from_bytes(self._read_byte(data, 8), 'big', signed=True))
			return key, o
		elif c == TAG_List:
			dt = self._read_byte(data)
			amt = int.from_bytes(self._read_byte(data, 4), 'big', signed=True)
			o = []
			for i in range(amt):
				o.append(self.__decode_value_type(data, dt))
			return key, o
		elif c == TAG_String:
			amt = int.from_bytes(self._read_byte(data, 2), 'big', signed=True)
			o = []
			for i in range(amt):
				o.append(self._read_byte(data))
		elif c == TAG_Compound:
			return key, self.__decode(data)
		else:
			raise ValueError(f"Invalid NBT entry type byte: {hex(c)}")

	def _read_key(self, data):
		if self._finished_reading:
			return ""
		size = int.from_bytes(self._read_byte(data, 2), 'big', signed=True)
		if size > 0:
			o = []
			for i in range(size):
				o.append(chr(self._read_byte(data)))
			return "".join(o)
		return ""

	def _read_byte(self, data, amt=1):
		if self._finished_reading:
			if amt <= 1:
				return 0
			else:
				return bytes(amt)
		if hasattr(data, "read"):
			if amt > 1:
				return data.read(amt)
			else:
				return data.read(1)[0]
		if len(data) > 0:
			if amt > 1:
				o = []
				for i in range(amt):
					o.append(data.pop(0))
				return o
			else:
				return data.pop(0)
		else:
			self._finished_reading = True
			return 0

	def _encode_type(self, v):
		if type(v) is int:
			if v >= -128 and v < 128:
				return TAG_Byte
			elif v >= -2**15 and v < 2**15:
				return TAG_Short
			elif v >= -2**31 and v < 2**31:
				return TAG_Int
			elif v >= -2**63 and v < 2**63:
				return TAG_Long
		elif type(v) is str:
			return TAG_String
		elif type(v) is float:
			return TAG_Float
		elif type(v) is list or type(v) is tuple:
			t = [type(_v) for _v in v]
			if not all([_t is t[0] for _t in t[1:]]):
				raise ValueError("failed to encode list: only lists containing a single type may be encoded")
			if type(t[0]) is int:
				if all([_v >= -128 and _v < 128 for _v in v]):
					return TAG_Byte_Array
				elif all([_v >= -2**31 and _v < 2**31 for _v in v]):
					return TAG_Int_Array
				else:
					return TAG_Long_Array
			return TAG_List
		elif type(v) is dict:
			return TAG_Compound
		elif type(v) is bytes or type(v) is bytearray:
			return TAG_Byte_Array
		else:
			raise TypeError(f"Failed to encode unsupported type: {type(v)}")

	def _encode_key(self, k):
		return list(len(k).to_bytes(2, 'big')) + list(bytes(k, 'UTF-8'))

	def _encode_value(self, v):
		if type(v) is int:
			if v >= -128 and v < 128:
				return list(v.to_bytes(1, 'big', signed=True))
			elif v >= -2**15 and v < 2**15:
				return list(v.to_bytes(2, 'big', signed=True))
			elif v >= -2**31 and v < 2**31:
				return list(v.to_bytes(4, 'big', signed=True))
			elif v >= -2**63 and v < 2**63:
				return list(v.to_bytes(8, 'big', signed=True))
			else:
				raise ValueError(f"failed to encode as signed 64-bit integer: {v}")
		elif type(v) is str:
			return list(len(v).to_bytes(2, 'big')) + list(bytes(v, 'UTF-8'))
		elif type(v) is float:
			return list(bytes(float(v)))
		elif type(v) is list or type(v) is tuple:
			if len(v) > 0:
				t = [type(_v) for _v in v]
				if not all([_t is t[0] for _t in t[1:]]):
					raise ValueError("failed to encode list: only lists containing a single type may be encoded")
				if type(t[0]) is int:
					if all([_v >= -128 and _v < 128 for _v in v]):
						return list(len(v).to_bytes(4, 'big', signed=True)) + \
								[_v.to_bytes(1, 'big', signed=True)[0] for _v in v]
					elif all([_v >= -2**31 and _v < 2**31 for _v in v]):
						return list(len(v).to_bytes(4, 'big', signed=True)) + \
								b"".join([_v.to_bytes(4, 'big', signed=True) for _v in v])
					else:
						return list(len(v).to_bytes(4, 'big', signed=True)) + \
								b"".join([_v.to_bytes(8, 'big', signed=True) for _v in v])
				else:
					return [self._encode_type(v[0])] + list(len(v).to_bytes(4, 'big', signed=True)) + \
							b"".join([self._encode_value(_v) for _v in v])
			return [TAG_End]
		elif type(v) is dict:
			o = [TAG_Compound, self._encode_key(k)]
			for _k in v.keys():
				o.extend(self._encode(_k, v[_k]))
		elif type(v) is bytes or type(v) is bytearray:
			return list(len(v).to_bytes(4, 'big', signed=True)) + list(v)
		else:
			raise TypeError(f"Failed to encode unsupported type: {type(v)}")

	def copy(self):
		return NBT(self)

