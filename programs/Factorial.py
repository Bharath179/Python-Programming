def fact(num):
    result=1
    while num>0:
        result=result*num
        num=num-1
    return result
for i in range(1,6):
 print("The factorial of",i,"is:",fact(i))
