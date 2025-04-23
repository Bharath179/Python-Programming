def lastword():
    s=input("Enter String...")
    words=s.split()
    last_word=words[-1]
    return len(last_word)
result=lastword()
print(result)