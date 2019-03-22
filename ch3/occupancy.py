
# a class to deal with occupancy problems 
import random 
from statistics import median
from statistics import mean

class Occupancy(): 

	def __init__(self, balls=0, bins=0):
		self.balls = balls
		self.bins = bins
		self.state = [0]*bins
		self.thrown = False

	# randomly throw the balls into bins 
	def throwBalls(self):
		self.thrown = True

		for i in range(self.balls):
			randBin = int(random.random() * self.bins)
			self.bins[randBin] += 1


	# max number of balls in a bin 
	def maxBalls(self):
		if self.thrown:
			return max(self.bins)
		else:
			print('please call throwBalls first')
		return 0

	# average number of balls in a bin 
	def avgBalls(self):
		if self.thrown:
			return mean(self.bins)
		else:
			print('please call throwBalls first')
		return 0

	# median number of balls in a bin 
	def medianBalls(self):
		if self.thrown:
			return median(self.bins)
		else:
			print('please call throwBalls first')
		return 0





