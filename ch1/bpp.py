import numpy as np

"""
In this algorithm, we divide the plane into segments such that each line 
segment lies in its own region in the plane, with no region of the plane
containing two line segments. We cut the plane with the lines l(s_i) for
1 <= i <= len(S), where S is the set of line segments. l(s_i) is the line
that is obtained by extending segment s_i on either side to infinity.

Input : a set S = {s_1, s_2, ... s_n} of non-intersecting line segments 
Output : a binary autopartition P_pi of S
"""
def BPP(S):
	# 1. Pick a permutation of pi of {1, 2, ... n} uniformly at random 
	# from n! possible permutations 
	pi = np.random.permutation(range(1, len(S) + 1))

	# 2. While a region contains > 1 segment, cut that region with the line 
	# l(s_i) where i is the first ordering in pi such that s_i cuts the region 
	regions = []


if __name__ == '__main__': 
	S = [(1,2), (4, 9), (12, 1)]
	BPP()