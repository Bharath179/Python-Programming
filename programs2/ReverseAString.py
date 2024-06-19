class Reverse:
   def reverse(self, s):
      temp = s.split(' ')
      temp = list(reversed(temp))
      return ' '.join(temp)
ob = Reverse()
sentence = "Learning Python is very Easy"
print(ob.reverse(sentence))
