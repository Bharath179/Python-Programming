"""class Solution:
    def isPalindrome(self, s:str):
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True"""


'''def sentence_palindrome(s):
    str= ""
    for c in s:
        if c.isalnum():
            str+= c.lower()
    reverse_str = str[::-1]
    return str==reverse_str


if __name__ == "__main__":
    str_ = "A man, a plan, a canal: Panama"
    if sentence_palindrome(str_):
        print("Sentence is palindrome")
    else:
        print("Sentence is not palindrome")'''

d={"abc":101,
   "bca":201
   }
print(d.get("abc"))

