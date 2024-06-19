import re

"""matcher=re.finditer("[abc]","a7b@k9z")
for match in matcher:
    print(match.start(),"...",match.group())"""


matcher=re.finditer("[^abc]","a7b@k9z")
for match in matcher:
    print(match.start(),"...",match.group())


matcher=re.finditer("[a-z]","a7b@k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer("[A-Z]","a7b@k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer("[a-zA-Z]","a7b@k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer("[a-zA-Z0-9]","a7b@k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer("[0-9]","a7b@k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer("[^a-zA-Z0-9]","a7b@k9z")
for match in matcher:
    print(match.start(),"...",match.group())

