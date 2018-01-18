from BowlingGame import Game
import unittest

class TestBowlingClass(unittest.TestCase):

	def setUp(self):
		self.game = Game()

	def test_gutter_game(self):
		self.roll_many(pins=0, times=20)

		self.assertEqual(self.game.score, 0)

	def test_all_ones(self):
		self.roll_many(pins=1, times=20)

		self.assertEqual(self.game.score, 20)

	def test_one_spare(self):
		self.roll_many(pins=5, times=2)
		self.game.roll(3)
		self.roll_many(pins=0, times=17)

		self.assertEqual(self.game.score, 16)

	def test_one_strike(self):
		self.game.roll(10)
		self.game.roll(3)
		self.game.roll(4)

		self.assertEqual(self.game.score, 24)

	def test_perfect_game(self):
		self.roll_many(pins=10, times=12)

		assert self.game.score == 300

	def roll_many(self, pins, times):
		for i in range(times):
			self.game.roll(pins)

if __name__ == '__main__':
	unittest.main()
