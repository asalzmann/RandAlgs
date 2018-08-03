"""
Date August 1, 2018 
Author Aidan Salzmann

mincut takes in a graph object, and attempts to find a mincut 
"""
from graph import DictGraph
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

"""
We repeat the following step: pick and edge uniformly at random 
and merge the two vertices at its endpoints. 

If, as a result, there are several edges between some pairs of 
vertices, retain them all. Edges between contracted vertices are 
removed such that there are no self loops. 

This process is called the 'contraction' of edges.

A key insight is that 'contractions' don't decrese the mincut. 

The algorithm continues until only two vertices remain, the edges
between them are taken as the min cut. 

Pr min cut found on a run = 2 / n(n-1) = O(1 / n^2)

Pr min cut found after n^2 / 2 runs = 1/e ~ 36%

We can improve this by running the algorithm more times. 
"""

def mincut(g):
	# check that g is a graph with > 2 vertices
	assert isinstance(g, nx.MultiGraph) and nx.is_connected(g)

	# check base cases of vertices 
	if g.number_of_nodes() < 2:
		return 0
	elif g.number_of_nodes() == 2:
		return g.size()

	# while more than two nodes remain remove an edge 
	while(g.number_of_nodes() > 2):
		# pick and edge at random
		idx = np.random.choice(len(g.edges()))
		random_edge = g.edges()[idx]

		# contract the edge in the graph
		#nx.draw(g)
		g = nx.contracted_edge(g, random_edge, self_loops=False)

	# return the number of edges remaining in g
	print(g)
	return g.size()
	

if __name__ == '__main__': 
	# multigraph instantiation using networkx (graph lib)
	mc_graph = nx.MultiGraph()
	mc_graph.add_nodes_from([1,2,3,4,5])
	mc_graph.add_edges_from([(1,2),(1,3),(2,3), (1,5), (2,4), (4,5), (4,5)])
	n = mc_graph.size()
	pr = 0
	bestcut = -1
	for i in range(30):
		currcut = mincut(mc_graph)
		if bestcut == -1 or currcut < bestcut:
			bestcut = currcut
		pr = 1 - (( 1 - (2 / float(n * (n-1))) ) ** i)
		print('Current min-cut found : {}'.format(bestcut))
		print('Probability this min-cut is the overall min-cut : {:.10%}'.format(pr))

	# for a more lightweight option, use the DictGraph class included
	# sample = {'A' : ['B', 'C', 'E'], 
	# 			'B' : ['C', 'D'], 
	# 			'C' : [], 
	# 			'D' : ['E'], 
	# 			'E' : ['D']}
	# mc_graph = DictGraph(sample)
