#Approach 1

mylist=[23, 65, 19, 90]
mylist[0],mylist[2]=mylist[2],mylist[0]
print("List after swapping:",mylist)

#Approach 2

mylist=[23, 65, 19, 90]
size=len(mylist)

temp=mylist[0]
mylist[0]=mylist[size-2]
mylist[size-2]=temp

print("List after swapping:",mylist)

#Approach 3
mylist=[23, 65, 19, 90]
get=(mylist[-2],mylist[0])
mylist[0],mylist[-2]=get
print("List after swapping:",mylist)