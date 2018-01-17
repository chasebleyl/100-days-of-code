class Game(object):
	def __init__(self):
		self.current_roll = 0
		self.rolls = [0 for i in range(21)]

	def roll(self, pins):
		self.rolls[self.current_roll] = pins
		self.current_roll += 1

	@property
	def score(self):
		score = 0
		frame_index = 0
		for frame in range(0, 10):
			if self.is_strike(frame_index):
				score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
				frame_index += 1
			elif self.is_spare(frame_index):
				score += 10 + self.rolls[frame_index + 2]
				frame_index += 2
			else:
				score += self.rolls[frame_index] + self.rolls[frame_index + 1]
				frame_index += 2
		return score

	def is_spare(self, frame_index):
		frame_score = self.rolls[frame_index] + self.rolls[frame_index + 1]
		if frame_score == 10:
			return True
		else:
			return False

	def is_strike(self, frame_index):
		if self.rolls[frame_index] == 10:
			return True
		else:
			return False
