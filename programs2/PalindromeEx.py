def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)-1)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")
"""
x = "malayalam"

w = ""
for i in x:
    w = i + w

if (x == w):
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")"""