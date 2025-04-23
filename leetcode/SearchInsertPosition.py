'''# Python program to implement
# the above approach

# Function to find insert position of K
def find_index(arr, n, K):

	# Lower and upper bounds
	start = 0
	end = n - 1

	# Traverse the search space
	while start<= end:

		mid =(start + end)//2

		if arr[mid] == K:
			return mid

		elif arr[mid] < K:
			start = mid + 1
		else:
			end = mid-1

	# Return the insert position
	return end + 1

# Driver Code
arr = [1, 3, 5, 6]
n = len(arr)
K = 2
print(find_index(arr, n, K))'''


# Function to find insert position of K
def find_index(arr, n, K):
    # Traverse the array
    for i in range(n):

        # If K is found
        if arr[i] == K:
            return i

        # If arr[i] exceeds K
        elif arr[i] > K:
            return i

    # If all array elements are smaller
    return n

# Driver Code
arr = [1, 3, 5, 6]
n = len(arr)
K = 6
print(find_index(arr, n, K))
