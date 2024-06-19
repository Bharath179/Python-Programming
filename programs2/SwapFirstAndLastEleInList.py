#Approach 1:Temporary Variable

"""mylist=[12,35,9,56,24]
size=len(mylist)

temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp

print("List after swapping:",mylist)"""

#Approach 2:
"""mylist=[12,35,9,56,24]
mylist[0],mylist[-1]=mylist[-1],mylist[0]
print("List after swapping:",mylist)"""

#Approach 3:using tuple
"""mylist=[12,35,9,56,24]
get=(mylist[-1],mylist[0])  #Packing 24 12
mylist[0],mylist[-1]=get
print("List after swapping:",mylist)"""



