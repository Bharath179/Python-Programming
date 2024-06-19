"""s=input("Enter string...")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)"""

"""string = input("Enter string...")
dups=[]
for ch in string:
  if string.count(ch)>1 and ch not in dups:
    dups.append(ch)
print('The duplicate characters are {}'.format(dups))"""


"""def remove_duplicates(input_string):
    return ''.join(set(input_string))

input_string = "hello"
result = remove_duplicates(input_string)
print(result)"""


s = input("Enter the string...")
newstr = ''
for letter in s:
	if letter not in newstr:
		newstr += letter
print("The string with duplicate letters removed:", newstr)
