def armstrong(num):
    sum=0
    temp=num
    while temp>0:
        x=temp%10
        sum=sum+x**3
        temp=temp//10
    if sum==num:
        print("The given number is armstrong number")
    else:
        print("The given number is not armstrong number")

armstrong(153)