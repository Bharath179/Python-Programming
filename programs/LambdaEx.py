#By using function
"""def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[2,4,5,7,8,9,10]
l1=list(filter(isEven,l))
print(l1)"""

#without using function
l=[2,4,5,7,8,9,10]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)

# By using map function with lambda
"""l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print(l1)"""

# Without using lambda
"""l=[1,2,3,4,5]
def doubleit(x):
    return 3*x
l1=list(map(doubleit,l))
print(l1)"""

# By using reduce function
from functools import reduce
l=[20,40,90,70]
l1=reduce(lambda x,y:x*y,l)
print(l1)

# By using range function
"""from functools import reduce
result=reduce(lambda x,y:x+y,range(1,101))
print(result)"""

# Generate the sequence of numbers in descending order
"""def countdown(num):
    print("Start count down")
    while(num>0):
     yield num
     num=num-1
result=countdown(5)
for x in result:
 print(x)"""

# Generate the sequence of numbers in Ascending order
def firstn(num):
    n=1
    while n<=num:
        yield n
        n=n+1
values=firstn(5)
for x in values:
 print(x)

