import numpy as np

def lazyselect(arr, length, k, universe):
	if arr == None:
		assert type(length) is int and type(k) is int and type(universe) is int
		arr = np.random.randint(0,universe,length)
	# 1 
	# pick n^(3/4) elements from S, chosen independently and uniformly
	# at random with replacement; call this multiset of elements R 
	draw = int(length**(3/4))

	P = [None]
	S_k = None

	

	while(len(P) > 4 * n**(3/4) + 2 or S_k not in P):
		P = []

		R = # take with replacement 'draw' elements 
		# 2 
		# sort R in O(n^(3/4)log(n)) steps using timsort 
		R = sorted(R)
		# 3
		# x = kn^(-1/4)
		# l = max(floor(x - root(n)), 1)
		# h = min(floor(x + root(n)), n^(3/4))
		# a = R_l
		# b = R_h
		# compare a and b to every element of S and determine 
		# r_s(a) and r_s(b)
		x = (int) k * (length ** (-1/4))
		l = max(np.floor(x - np.sqrt(length)), 1)
		h = min(np.ceiling(x + np.sqrt(length)), (int) n ** (3/4))
		a = R[l + 1]
		b = R[h + 1]

		a_rank = 0
		b_rank = 0

		for elem in arr:
			if elem < a:
				a_rank += 1
			if elem < b:
				b_rank += 1
		# 4
		small_n = n ** 1/4
		if k < small_n:
			for elem in arr:
				if elem <= b:
					P.append(elem)
		elif k > n - small_n:
			for elem in arr:
				if a <= elem:
					P.append(elem)
		elif ((n - small_n) < k) and (k < small_n): 
			for elem in arr:
				if a <= elem <= b:
					P.append(elem)

	# 5
	# by sorting P in O(P log P) steps, identify P_(k-r_s(a) + 1)
	# which is S_k
	P = sorted(P)
	S_k = P[k - a_rank + 1]
	return S_k


if __name__ == '__main__': 
	lazyselect(None, 100, 30, 200)