class Goalie(object):
	def __init__(self,team,name, pos):
		self.name = name
		self.team = team
		if self.team == 1:
			self.position = fieldGolPos1[pos]
		else: self.position = fieldGolPos2[pos]
		self.image = PygameGame.fieldGoalImages[name]
		self.rect = 
		self.velocity = goalVelocity[name]
		self.power = goalPower[name]

class Defender(object):
	def __init__(self,team,name,pos):
		self.name = name
		self.team = team
		if self.team == 1:
			self.position = fieldDefPos1[pos]
		else: self.position = fieldDefPos2[pos]
		self.image = PygameGame.fieldDefImages[name]
		self.rect = 
		self.velocity =defenseVelocity[name]
		self.power = defensePower[name]

class Midfielder(object):
	def __init__(self,team,name,pos):
		self.name = name
		self.team = team
		if self.team == 1:
			self.position = fieldMidPos1[pos]
		else: self.position = fieldMidPos2[pos]
		self.image = PygameGame.fieldMidImages[name]
		self.rect = 
		self.velocity =midfieldVelocity[name]
		self.power = midfieldPower[name]

class Attacker(object):
	def __init__(self,team,name,pos):
		self.name = name
		self.team = team
		if self.team == 1:
			self.position = fieldAttPos1[pos]
		else: self.position = fieldAttPos2[pos]
		self.image = PygameGame.fieldAttImages[name]
		self.rect = 
		self.velocity =attackVelocity[name]
		self.power = attackPower[name]

