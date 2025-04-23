#Approach 1
'''list = [4, 5, 6, 7, 8, 9]
print(list[::-1])'''

#Approach 2
lst = [4, 5, 6, 7, 8, 9]
size = len(list)
for i in range(0, size):
    for j in range(i + 1, size):
        if lst[i] < lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
    print(list[i])
