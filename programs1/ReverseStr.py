
def reverseString(x):
    # Declaring an empty String
    NewString = ""
    # Traversing through individual characters in a string
    for i in x:
        # Add the character to the empty string
        NewString = i + NewString
    # return the new string
    return NewString
# Sample String
x = "Dextris Software Solutions"
# Function Call
ReversedString = reverseString(x)
# Printing Output
print(ReversedString)

#H e l l o
#H
#e H
#l e H
#l l e H
#o l l e H

'''s="Dextris Software Solutions"
s1=s.split()
print(s1[::-1])'''

s=input("Enter Some String:")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)

