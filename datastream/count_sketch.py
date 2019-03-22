"""
Author: Aidan Salzmann
This is a simple implementation of a basic sketch and the count sketch.
"""
import numpy 

"""
This program finds the next prime number greater than num. 

TODO: Improve this by implementing a sieve or other efficent method to 
find the next prime. 
"""
def is_prime(num):
	if x >= 2:
        for y in range(2,num):
            if not (x % y):
                return False
    else:
		return False
    return True

def generate_next_prime(num):
	while(True):
		if is_prime(num):
			return num
		num += 1

"""
The basic sketch takes a parameter epsilon, which should be though of as
small and postive. 

The hash family we will choose hash functions from is 
h_a(x) = (ax mod p) mod m
where our universe is {0, ..., m} and p is a prime >= m. 

"""
def basic_sketch(epsilon, M, datastream):
	# Initialize 
	k = 3/(epsilon**2)
	C = [0] * k
	p = find_next_prime(M)
	p2 = 3
	a = numpy.randint(0, M, 1) % p
	b = numpy.randint(0, 2, 1) % p
	# Choose a random hash function h : [n] -> [k], 2-universal 
	h = lambda x: ((a * x) % p) % M
	# Choose a random hash function g : [n] ->  {-1,1}, 2-universal 
	g = lambda x: ((b * x) % p) % M
	# Process
	# Because we're considering ints, the count of a token is always one
	_c = 1
	
	for data in datastream:
		C[h(j)] = C[h(j)] + _c * g(j)
	# Output 
	# One query a, report f_hat_a = g(a)C[h(a)] 
	return C, g, h

def main():
	file = open('data.txt', 'r')
	data = file.readlines()
	file.close()
	basic_sketch(0.05, 200, data)


if __name__ == '__main__':