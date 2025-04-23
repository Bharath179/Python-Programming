# Sum of dictionary

'''def returnsum(dict):
    sum=0
    for i in dict.values():
        sum=sum+i
    return sum

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnsum(dict))'''

'''def returnSum(dict):
    sum = 0
    for i in dict:
        sum = sum + dict[i]
    return sum
    
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))'''

# Ways to remove a key from dictionary

'''test_dict = {"Aravind": 22, "Mani": 21, "Hanuman": 21}

print("The dictionary before performing remove is : ", test_dict)

# Using del to remove a dict
# removes Mani
del test_dict['Mani']

# Printing dictionary after removal
print("The dictionary after remove is : ", test_dict)'''

d={"Bharath":27,"Kumar":25,"Reddy":20}
removed_value=d.pop('Reddy')
print("The dictionary after remove is : " + str(d))
print("The removed key's value is : " + str(removed_value))


