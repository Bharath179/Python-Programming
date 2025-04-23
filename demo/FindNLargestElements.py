# Python program to find N largest
# element from given list of integers

# Function returns N largest elements


def Nmaxelements(list1, n):
	final_list = []
	for i in range(0, n):
		max1 = 0
		for j in range(len(list1)):
			if list1[j] > max1:
				max1 = list1[j]
		list1.remove(max1)
		final_list.append(max1)
	print(final_list)
# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
n = 1
# Calling the function
Nmaxelements(list1, n)

"""d={100:'durga' ,200:'ravi', 300:'shiva'}

#print(d[100]) #durga
for k,v in d.items():
    print(k,v)"""

