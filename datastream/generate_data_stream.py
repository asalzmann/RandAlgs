#!/usr/bin/python

"""
Write random data to the data.txt file 
takes in a universe size M, writes n 
random digits to the universe M
"""

import argparse
import numpy as np

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--M', metavar='M', type=int, default=100,
						 help='The size of the universe - data written ranges from 0, ..., M-1')
	parser.add_argument('--n', metavar='n', type=int, default=300, 
							help='The number of integers to write to the data.txt file')
	args = parser.parse_args()

	File_object = open('data.txt','w+')
	M = args.M
	n = args.n

	datastream = np.random.randint(0, M-1, n)

	for data in datastream:
		File_object.write(str(data) + ' ')
		
	File_object.close()

if __name__ == '__main__':
	main()