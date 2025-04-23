import re
result = re.match(r'abc', 'abcdef')
if result:
    print("Match found:", result.group())

result = re.search(r'abc', 'xyzabcdef')
if result:
    print("Match found:", result.group())

result = re.findall(r'\D+', '123 abc 456 def 789')
print(result)  # Output: ['123', '456', '789']

matches = re.finditer(r'\d+', '123 abc 456 def 789')
for match in matches:
    print(match.group())

result = re.sub(r'\d+', 'NUM', 'abc 123 def 456')
print(result)  # Output: 'abc NUM def NUM'

result = re.split(r'\s+', 'This is a sentence.')
print(result)  # Output: ['This', 'is', 'a', 'sentence.']