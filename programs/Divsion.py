num1=int(input("Enter stating number..."))
num2=int(input("Enter last number..."))
for i in range(num1, num2+1):
    if((i%8==0)&(i%5==0)):
        print(i)


