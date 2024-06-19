def linear_Search(list, n, key):

    for i in range(0, n):
        if (list[i] == key):
            return i
    return -1


list = [1, 3, 5, 4, 7, 9]
key = 4

n = len(list)
res = linear_Search(list, n, key)
if (res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)