list1=[10,20,30,40,50,20,10]
for i in range(0,len(list1)):
   for j in range(i+1,len(list1)):
    if list1[i]==list1[j]:
     print(list1[i])

"""a,b= [int(x) for x in input("Enter 2 numbers :").split()]
print("product of:",a**b)"""

"""import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)"""