import re

# Pre-Defined Character Classes
matcher=re.finditer('\s',"a7b @k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer('\d',"a7b @k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer('\w',"a7b @k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer('\S',"a7b @k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer('\D',"a7b @k9z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher=re.finditer('.',"a7b @k9z")
for match in matcher:
    print(match.start(),"...",match.group())
