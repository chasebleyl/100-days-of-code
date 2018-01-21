class Game(object):

	def __init__(self):
		self.current_roll = 0
		self.rolls = [0 for i in range(21)]

	@property
	def score(self):
		score = 0
		roll_index = 0
		for frame in range(10):
			if self.is_strike(roll_index):
				score += self.get_strike_frame_score(roll_index)
				roll_index += 1
			elif self.is_spare(roll_index):
				score += self.get_spare_frame_score(roll_index)
				roll_index += 2
			else:
				score += self.get_regular_frame_score(roll_index)
				roll_index += 2
		return score

	def is_strike(self, roll_index):
		if self.rolls[roll_index] == 10:
 			return True
		else:
			return False

	def is_spare(self, roll_index):
		if self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
 			return True
		else:
			return False
	
	def get_strike_frame_score(self, roll_index):
		return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]	
	
	def get_spare_frame_score(self, roll_index):
		return 10 + self.rolls[roll_index + 2]	

	def get_regular_frame_score(self, roll_index):
		return self.rolls[roll_index] + self.rolls[roll_index + 1]

	def roll(self, pins):
		self.rolls[self.current_roll] = pins
		self.current_roll += 1
