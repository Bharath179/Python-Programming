'''def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))'''

'''d={"swift":100,"BMW":200,"Kia":300}

print(d.get[100])'''

'''input_string = input("Enter a dictionary: ")

# Converting the input string to a dictionary
input_dict = eval(input_string)

# Creating a new dictionary with only the key 'swift'
output_dict = {"swift": input_dict.get("swift")}

# Printing the output dictionary
print(output_dict)


input_string = input("Enter a dictionary: ")

# Converting the input string to a dictionary
input_dict = eval(input_string)

# Printing the value associated with the key 'swift'
print(input_dict.get("swift"))
'''

# Python3 code to demonstrate working of
# Get values of particular key in list of dictionaries

'''res = {}
# initializing list
test_list = [{'swift': 100, 'MahendraThar': 200, 'Audi': 300},
			{'Jaguar': 400}, {'KIA': 500, 'BMW': 4000}]
# printing original list
#print("The original list is : " + str(test_list))

for i in test_list:
	for j in i:
		if j in res.keys():
			res[j].append(i[j])
		else:
			res[j] = [i[j]]
# printing result
print("The values corresponding to key : " + str(res['BMW']))'''


def get_values(lst, key):
	result = []
	for dictionary in lst:
		if key in dictionary:
			result.append(dictionary[key])
	return result

# Initialize list
test_list = [{'Swift': 100, 'BMW': 200, 'MahendraThar': 300}]
# Get values of 'gfg' key
res = get_values(test_list, 'MahendraThar')
# Print the result
print("The values corresponding to key : " + str(res))

