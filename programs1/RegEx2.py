import re

# Functions of re module

#1)match()===>It will check the given pattern at beginning of target string
"""s=input("Enter pattern to match...")
m=re.match(s,"abcdefgh")
if m!=None:
    print("Match is available at the beginning of the string")
    print('start Index:{} and end Index:{}'.format(m.start(),m.end()))
else:
    print("Match is not available at the beginning of the string")

#2)fullmatch()===>It will check the given pattern to all of target string
s=input("Enter pattern to match...")
m=re.fullmatch(s,"abcdefgh")
if m!=None:
    print("Full string matched")
else:
    print("Full string not matched")"""

#3)search()===>It is used to check the given pattern in the target string
'''s=input("Enter pattern to match...")
m=re.search(s,"abaaaba")
if m!=None:
    print("Match Available")
    print("First occurrence of match with start index:",m.start(),"and end index:",m.end())
else:
    print("Match is not Available")'''

#4)findall()===>To find all occurrences of the match
"""l=re.findall("[0-9]","a7b9c5kz")
print(l)"""

#5)sub()===>It will replace the every matched pattern with provided replacement
"""s=re.sub("[a-z]","-","a7b9c5k8z")
print(s)"""

#6)subn()===>It exactly same as sub but it can also returns no of replacements
"""t=re.subn("[a-z]","#","a7b9c5k8z")
print(t)"""

#7)split()===>It will split the given target string to particular pattern
"""t=re.split(",","Bharath,Kumar,Reddy,Vidya")
print(t)
for l in t:
    print(l)"""

"""import re

# initialising string
ini_string = "abcjw:, .@! eiw"

# printing initial string
print("initial string : ", ini_string)

result = re.sub('\W', '', ini_string)

# printing final string
print("final string", result)"""

import re

# define a function
def find(string, sample):
    # check substring present
    # in a string or not
    if (sample in string):
        y = "^" + sample
        # check if string starts
        # with the substring
        x = re.search(y, string)

        if x:
            print("string starts with the given substring")

        else:
            print("string doesn't start with the given substring")

    else:
        print("entered string isn't a substring")
# Driver code
string = "geeks for geeks makes learning fun"
sample = "geeks"
# function call
find(string, sample)

sample = "makes"

# function call
find(string, sample)