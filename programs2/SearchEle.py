#Approach 1:

mylist=[1,6,3,5,3,4]
ele=5
flag=0

for i in mylist:
 if(i==ele):
    print("Element found")
    flag=1
    break
if(flag==0):
        print("Element not found")