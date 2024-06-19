"""s={2,3,4,2,5,6,7,4}
print(s)"""

#Important functions of set
#1)add()
"""s={20,30,40,50}
s.add(10)
print(s)"""

#2)update(x,y,z)
"""s={20,30,40,50}
l=[70,80,90]
s.update(l,range(5))
print(s)"""

#3)copy()
"""s={10,20,30}
s1=s.copy()
print(s1)"""

#4)pop()===>It removes and returns some random element from the set
"""s={10,20,30,40}
print(s)
print(s.pop())
print(s)"""

#5)remove()==>It removes specified element from the set
"""s={10,20,30,40}
print(s)
print(s.remove(30))
print(s)"""

#6)discard()==>It removes the specified element from the set
"""s={10,20,30,40}
print(s)
print(s.discard(50))
print(s)"""

#7)clear()==>It removes all elements from the set

#Mathematical operations on the set

#1)Union()==>We can use this function to return all elements present in both sets
s1={10,20,30}
s2={40,50,60}
print(s1|s2)

#2)Intersection()==>Returns common elements present in both x and y
s1={10,20,30,40}
s2={40,50,60}
print(s1&s2)

#3)difference()==>Returns the elements present in x but not in y
s1={10,20,30,40}
s2={40,50,60}
print(s1-s2)

#4)Symmetric difference()==>Returns elements present in either x or y but not in both
s1={10,20,30,40}
s2={40,50,60,70}
print(s1^s2)

#Membership operators(in,not in)
"""s=set("Bharath")
print(s)
print('b'in s)
print('B'in s)"""

#set comprehension
"""s={x:x*x for x in range(5)}
print(s)"""

#Vowel program
"""w=input("Enter word to search for vowels: ")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("The different vowel's present in",w,"are",d)"""
