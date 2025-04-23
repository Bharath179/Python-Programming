"""s=input("Enter some string...")
i=0
for x in s:
    print("The character present at positive index {} and at negative index {} is {}".format(i,i-len(s),x))
    i=i+1"""

"""import re
s=input("Enter number...")
m=re.fullmatch("[7-9]\d{9}",s)
if m!=None:
    print("Number is valid")
else:
    print("Number is invalid")"""

import re
n=input("Enter email ID...")
m=re.fullmatch("\w[a-z0-9]*@gmail[.]com",n)
if m!=None:
    print("Email Id is valid")
else:
    print("Email Id is not valid")




