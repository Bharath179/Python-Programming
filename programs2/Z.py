"""s=input("Enter string...")
alphabets=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output=''.join(sorted(alphabets)+sorted(digits))
print(output)"""

a="Hello World"
u,l=0,0
for ch in a:
    if ch.isupper():
        u+=1
    elif ch.islower():
        l+=1
print(f'Upper case char={u}')
print(f'Lower case char={l}')
