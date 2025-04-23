# Program for Iterative Binary Search Function


"""1.Compare x with the middle element.
2.If x matches with the middle element, we return the mid index.
3.Else if x is greater than the mid element,
then x can only lie in the right (greater) half subarray after the mid element.
Then we apply the algorithm again for the right half.
4.Else if x is smaller, the target x must lie in the left (lower) half.
So we apply the algorithm for the left half"""


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

# Test array
arr = [2, 3, 4, 10, 40]
x = 11

# Function call
result = binary_search(arr, x)
print(result)
"""
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")"""


"""Execution of the binary_search function:
Initial values:

low = 0
high = 4 (because len(arr) - 1 = 4)
x = 10
First Iteration:

mid = (0 + 4) // 2 = 2 (middle index).
arr[mid] = arr[2] = 4, which is less than x = 10.
Since arr[mid] < x, we set low = mid + 1 = 3.
Second Iteration:

Now, low = 3, high = 4.
mid = (3 + 4) // 2 = 3 (middle index).
arr[mid] = arr[3] = 10, which is equal to x = 10.
We have found x at index 3, so the function returns 3.
"""

