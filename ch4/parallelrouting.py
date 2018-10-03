""" A hypercube class """

class Hypercube(object):
	def __init__(self, dimensions=1):
		num_nodes = 2**dimensions
		