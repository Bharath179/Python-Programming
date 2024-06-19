"""class fib:
    a,b,=0,1
    print(a)
    print(b)
    for i in range(2,10):
        c=a+b
        a=b
        b=c
        print(c)"""

"""s="Learning Python is very very easy!!!"
print(s[1:7:3])"""

"""city=input("Enter your city Name:")
scity=city.strip()
if scity=='Hyderabad':
 print("Hello Hyderbadi..Adab")
elif scity=='Chennai':
 print("Hello Madrasi...Vanakkam")
elif scity=="Bangalore":
 print("Hello Kannadiga...Shubhodaya")
else:
 print("your entered city is invalid")"""

"""s=" My dear friend "
print(s.rstrip())"""

s=input("Enter main string:")
subs=input("Enter sub string:")
flag=False
pos=-1
n=len(s)
while True:
 pos=s.find(subs,pos+1,n)
 if pos==-1:
  break
 print("Found at position",pos)
flag=True
if flag==False:
 print("Not Found")
