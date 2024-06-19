list1=[2,3,5,6,7]
searchable_ele=3
flag = False
for i in range(0,len(list1)+1):
    if searchable_ele==list1[i]:
        print("Element found at index:",i)
        flag=True
        break
if flag==False:
    print("Element not found...")
