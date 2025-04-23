def length_of_last_word(s):
    length=0
    i=len(s)-1
    while i>=0 and s[i]==' ':
        i-=1
    while i>=0 and s[i]!=' ':
        length+=1
        i-=1
    return length
print(length_of_last_word("Hello World"))
print(length_of_last_word("  fly me to  the moon"))