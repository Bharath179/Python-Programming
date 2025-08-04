def non_repeating(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            return s[i]
    return None

print(non_repeating('aadfte'))