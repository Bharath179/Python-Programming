"""list=[10,20,30,40]
t=tuple(list)
print(t)

t=tuple(range(10,20,2))
print(t)"""



# Accessing Elements using index or by using slice operator
"""t=(10,30,40,60,20,80)
print(t[2])
print(t[-1])
print(t[1:5])
print(t[1:-4])"""

# Mathematical operators for tuple + and *(repetation operator)
"""t1=(10,30,40,60,20,80)
t2=(2,3,4,5)
print(t1+t2)
print(t2*2)"""

# Important functions of tuple
"""t2=(2,3,4,5)
print(len(t2))"""

#count ===> Returns number of occurences of given element in tuple
"""t2=(2,3,4,5,6,2)
print(t2.count(2))"""

#index()===> Returns index of first occurence of given element
"""t=(10,20,10,30,40)
print(t.index(10))"""

#sorted()===> To sort elements based on default natural sorting order
"""t=(10,20,40,30,50)
t1=sorted(t)
print(t1)"""

# We can sort according to reverse of default natural sorting order as follows
"""t=(10,20,30,40)
t1=sorted(t,reverse=True)
print(t1)"""

# Min() and Max functions
"""t=(10,20,30,40)
print(min(t))
print(max(t))"""

# Tuple packing and UnPacking
"""a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)"""

"""t=(10,20,30,40)
a,b,c,d=t
print(a,b,c,d)"""

# Tuple Comprehension ===> is not possible for tuple
"""t=(x**2 for x in range(1,6))
print(type(t))         # ===>Getting generator object
for x in t:
    print(x)"""

t=eval(input("Enter Tuple of Numbers:"))
l=len(t)
sum=0
for x in t:
    sum=sum+1
print("The sum=",sum)
print("The average=",sum/l)