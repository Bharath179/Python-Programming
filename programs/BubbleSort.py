
list1=[5,4,2,1,8]
print("Unsorted list:",list1)
for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("sorted list:",list1)



'''num=int(input("How many elements you want to enter:"))
for k in range(num):
   list1.append(int(input()))'''

