""" 
Date: Aug 1, 2018
Author: Aidan Salzmann

This class describes a basic graph which is useful 
in implementing many of the randomized algorithms that 
occur in this project 
"""

class RandomGraph(object):

	class Node(object):
		def __init__(self, edges=None):
			if edges == None:
				edges = None
			self.__edges = edges

	def __init__(self, graph_size=None, density=None):
		""" initializes a graph object 
		If no dictionary or None is given,  
		an empty dictionary will be used"""
		if graph_size == None:
			graph_size = 0
		self.__graph_size = graph_size

	def vertices(self):
		""" returns the vertices of a graph """
		return list(self.__graph_dict.keys())

	def edges(self):
		""" returns the edges of a graph """
		return self.__generate_edges()

	def add_vertex(self, vertex):
		""" If the vertex "vertex" is not in 
			self.__graph_dict, a key "vertex" with an empty
			list as a value is added to the dictionary. 
			Otherwise nothing has to be done. 
		"""
		if vertex not in self.__graph_dict:
			self.__graph_dict[vertex] = []

	def add_edge(self, edge):
		""" assumes that edge is of type set, tuple or list; 
			between two vertices can be multiple edges! 
		"""
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.__graph_dict:
			self.__graph_dict[vertex1].append(vertex2)
		else:
			self.__graph_dict[vertex1] = [vertex2]

	def __generate_edges(self):
		""" A static method generating the edges of the 
			graph "graph". Edges are represented as sets 
			with one (a loop back to the vertex) or two 
			vertices 
		"""
		edges = []
		for vertex in self.__graph_dict:
			for neighbour in self.__graph_dict[vertex]:
				if {neighbour, vertex} not in edges:
					edges.append({vertex, neighbour})
		return edges

	def __str__(self):
		res = "vertices: "
		for k in self.__graph_dict:
			res += str(k) + " "
		res += "\nedges: "
		for edge in self.__generate_edges():
			res += str(edge) + " "
		return res

class DictGraph(object):
	def __init__(self, graph_dict=None):
		""" initializes a graph object 
		If no dictionary or None is given,  
		an empty dictionary will be used"""
		if graph_dict == None:
			graph_dict = {}
		self.__graph_dict = graph_dict

	def vertices(self):
		""" returns the vertices of a graph """
		return list(self.__graph_dict.keys())

	def num_vertices(self):
		""" returns the # of vertices of a graph """
		return len(self.__graph_dict.keys())

	def edges(self):
		""" returns the edges of a graph """
		return self.__generate_edges()

	def add_vertex(self, vertex):
		""" If the vertex "vertex" is not in 
			self.__graph_dict, a key "vertex" with an empty
			list as a value is added to the dictionary. 
			Otherwise nothing has to be done. 
		"""
		if vertex not in self.__graph_dict:
			self.__graph_dict[vertex] = []

	def add_edge(self, edge):
		""" assumes that edge is of type set, tuple or list; 
			between two vertices can be multiple edges! 
		"""
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.__graph_dict:
			self.__graph_dict[vertex1].append(vertex2)
		else:
			self.__graph_dict[vertex1] = [vertex2]

	def __generate_edges(self):
		""" A static method generating the edges of the 
			graph "graph". Edges are represented as sets 
			with one (a loop back to the vertex) or two 
			vertices 
		"""
		edges = []
		for vertex in self.__graph_dict:
			for neighbour in self.__graph_dict[vertex]:
				if {neighbour, vertex} not in edges:
					edges.append({vertex, neighbour})
		return edges

	def __str__(self):
		res = "vertices: "
		for k in self.__graph_dict:
			res += str(k) + " "
		res += "\nedges: "
		for edge in self.__generate_edges():
			res += str(edge) + " "
		return res