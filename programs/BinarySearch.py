def BinarySearch(list1,key):
    low=0
    high=len(list1)-1
    flag=False
    while low<=high and not flag:
        mid=(low+high)//2
        if key==list1[mid]:
            flag=True
        elif key>list1[mid]:
            low=mid+1
        else:
            high=mid-1
    if flag==True:
        print("Key is found")
    else:
        print("Key is not found")

list1=[23,1,4,5,6]
list1.sort()
print(list1)
key=int(input("Enter the Key:"))
BinarySearch(list1,key)