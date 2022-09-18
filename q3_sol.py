def Median(arr):
	n = len(arr)
	# If length of array is even
	if n % 2 == 0:
		x = n // 2
		y = arr[x]
		z = arr[x - 1]
		result = (y + z) / 2
		return result
		
	# If length of array is odd
	else:
		x = n // 2
		result = arr[x]
		return result


if __name__ == "__main__":
	arr1 = [ 1,2,3 ]
	arr2 = [ 4,5 ]
	# Concatenating arrays
	arr3 = arr1 + arr2
	# Sorting the resultant array
	arr3.sort()
	print("Median of arrays is = ", Median(arr3))
