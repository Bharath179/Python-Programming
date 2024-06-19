#Approach 1
'''list = [4, 5, 6, 7, 8, 9]
print(list[::-1])'''

#Approach 2
list = [4, 5, 6, 7, 8, 9,]
size=len(list)
for i in range(0,size):
    for j in range(i+1,size):
     if list[i]<list[j]:
         temp=list[i]
         list[i]=list[j]
         list[j]=temp
    print(list[i])
