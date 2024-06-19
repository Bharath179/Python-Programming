"""s=input("Enter string...")
even_string=[]
odd_string=[]
for i in range(len(s)):
    if i%2==0:
        even_string.append(s[i])
    else:
        odd_string.append(s[i])
print("odd characters:{}".format(odd_string))
print("even characters:{}".format(even_string))"""


list1="Geeksforgeeks"
list2 = [x for ind, x in enumerate(list1) if ind%2==0]
list3 = [x for ind, x in enumerate(list1) if ind%2!=0]
print(list2)
print(list3)

