def binary_search(arr,low,high,key):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binary_search(arr,low,mid-1,key)
        else:
            return binary_search(arr,high,mid+1,key)

arr=[30,40,20,10,50]
arr.sort()
key=90

#Function call
result=binary_search(arr,0,len(arr)-1,key)
if result !=-1:
    print("The element is found at index:"+str(result))
else:
    print("The element is not found at index:")
