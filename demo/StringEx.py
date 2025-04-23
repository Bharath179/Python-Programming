# Reverse String
def reverse_string(str):
    return str[::-1]
input_string="hello"
print("Reversed string is:",reverse_string(input_string))

# Duplicates in string
def duplicates(s):
    result=""
    for char in s:
        if char not in result:
            result=result+char
    return result
input_char="programming"
print("Duplicates characters are:",duplicates(input_char))

# First non-repeating character
def non_repeating(s):
    for char in s:
        if s.count(char)==1:
            return char
    return None
input_string="swiss"
print("The first non-repeating character is:",non_repeating(input_string))

# Find all occurence of the substring
def find_all_index(s,substring):
    indicies=[]
    index=s.find(substring)
    while index != -1:
        indicies.append(index)
        index=s.find(substring,index+1)
    return indicies
input_string="abcdabc"
substring="abc"
print(f"Occurrences of '{substring}': {find_all_index(input_string, substring)}")

# Palindrome String(two pointer method)
def is_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left=left+1
        right=right-1
    return True
input_string="banana"
if is_palindrome(input_string):
    print("The string is palindrome.")
else:
    print("The string is not palindrome")

# Anagrams check
def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    for char in s1:
        if s1.count(char)!=s2.count(char):
            return False
    return True
string1="listen"
string2="silent"
if is_anagram(string1,string2):
    print("The passed strings are anagrams")
else:
    print("The passed strings are not anagrams")