import numpy as np
	
'''
* Execution of this function happens in 3 steps 
* 1) We choose a random pivot
* 2) We put the array into a set less than the pivot
*    and a set greater than the pivot 
* 3) 
'''
def quicksort(arr=None):
	if arr is None:
		# If no array is passed, initialize a random array 
		arr = np.random.randint(0,200,10)

	if len(arr) == 1 or len(arr) == 0:
		return arr
	# Randomly pick a pivot 
	i = np.random.randint(len(arr))
	pivot = arr[i]
	# compare the elements to the pivot to get the elements smaller
	less_than = [element for element in arr if element < pivot]
	# the pivots 
	pivots = [element for element in arr if element == pivot]
	# and greater than the pivot 
	greater_than = [element for element in arr if element > pivot]
	return quicksort(less_than) + pivots + quicksort(greater_than)


if __name__ == '__main__': 
	array = [101, 100, 22, 97, 204, 42]
	print("Array before sort : {}".format(array))
	sorted_array = quicksort(array)
	print("Array after sort : {}".format(sorted_array))


