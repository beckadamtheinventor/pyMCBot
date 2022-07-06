
class Block:
	def __init__(self, id, metadata, name, title, is_full_block=True, mining_level=0, iswater=False, islava=False):
		self.id = id
		self.metadata = metadata
		self.name = name
		self.title = title
		self.is_full_block = is_full_block
		self.mining_level = mining_level
		self.iswater = iswater
		self.islava = islava
