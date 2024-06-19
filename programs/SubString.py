str1=input("Enter the String...")
for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        print(str1[i:j],end="  ")
        print()