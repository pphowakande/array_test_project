#!/usr/bin/env python

def flatten_array(input_array):
	""" function to flatten an array of arbitrarily nested arrays of integers
		into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].
	"""
	results = []

	if type(input_array) != type([]):
		# return single element array if we are not passed an array
		results = [input_array]
	else:
		# add each element to the results, recurse if the element is another array
		for element in input_array:
			results += flatten_array(element) if type(element) == type([]) else [element]

	return results

if __name__ == '__main__':
	""" Script test entry point
	"""
	test_array = [[1,2,[3]],4]

	if flatten_array(test_array) == [1,2,3,4]:
		print 'success'
	else:
		print 'fail'

	print flatten_array(test_array)

	# couple of other tests...
	test_array = [[1,2,[3]],[[4,5,[6]],[[7,8,[9]],10]]]
	print flatten_array(test_array)

	test_array = [[1,2,[[3,4,[[5,6,[[7,8,[9]],10]],11]],12]],13]
print flatten_array(test_array)
