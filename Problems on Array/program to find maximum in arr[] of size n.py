# Python3 program to find maximum in arr[] of size n


# Function to find maximum in arr[] of size n
def largest(arr, n):
	
	# Initialize maximum element
	mx = arr[0]

	# Traverse array elements from second
	# and compare every element with
	# current max
	for i in range(1, n):
		if arr[i] > mx:
			mx = arr[i]

	return mx


# Driver Code
if __name__ == '__main__':
	arr = [10, 324, 45, 90, 9808]
	n = len(arr)
	
	# Calculating length of an array
	Ans = largest(arr, n)
	
	# display max
	print("Largest in given array is", Ans)


# This code is contributed by Jai Parkash Bhardwaj
# and improved by prophet1999
