
class Entity:
	def __init__(self, id, is_player=False, is_hostile=False, is_passive=False, is_neutral=False):
		self.id = id
		self.is_player = is_player
		self.is_hostile = is_hostile
		self.is_passive = is_passive
		self.is_neutral = is_neutral
