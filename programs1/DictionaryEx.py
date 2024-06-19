"""d={10:'Bharath',20:"Kumar",30:"Reddy"}
print(d)"""

# Accessing elements from the dictionary
# 1) By using Keys
"""d={10:'Bharath',20:"Kumar",30:"Reddy"}
print(d[10])
if 40 in d:
 print(d[40])"""

# Update Dictionaries
"""d={10:'Bharath',20:"Kumar",30:"Reddy"}
print(d)
d[40]='Vidya'
print(d)
d[10]='Lakshmi'
print(d)"""

# Delete elements from dictionary
"""d={10:'Bharath',20:"Kumar",30:"Reddy"}
print(d)
del d[30]
print(d)"""

#clear()===> remove all enteries from the dictionary
"""d={10:'Bharath',20:"Kumar",30:"Reddy"}
print(d)
d.clear()
print(d)"""

#del d===>To delete total dictionary
"""d={10:'Bharath',20:"Kumar",30:"Reddy"}
print(d)
del d
print(d)"""

# Important functions of dictionary
# 1)dict()
d=dict() #===>It creates empty dictionary
d=dict({100:"durga",200:"ravi"}) #==>It creates dictionary with specified elements
d=dict([(100,"durga"),(200,"shiva"),(300,"ravi")])  #==>It creates dictionary with the given list of tuple elements

# 2)len()   # 3)clear()

#4)get()
"""d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d[100])
print(d.get(100))
print(d.get(400))
print(d.get(100,"Guest"))
print(d.get(400,"Guest"))
#print(d[400])"""

#5)pop()
"""d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d.pop(100))
print(d)
print(d.pop(400))"""

#6)popItem()==>It removes an arbitrary item(key-value) from the dictionaty and returns it.
"""d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d)
print(d.popitem())
print(d)"""

#7)Keys()==>It returns all keys associated with dictionary
"""d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d)
print(d.keys())
for k in d.keys():
    print(k)"""

#8)values()==>It returns all values associated with the dictionary
"""d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d)
print(d.values())
for k in d.values():
    print(k)"""

#9)items()==>It returns list of tuples representing key-value pairs
"""d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d)
print(d.items())"""

#10)copy()==>To create exactly duplicate dictionary(cloned copy)
"""d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d)
d1=d.copy()
print(d1)"""

#11)setdefault()
"""d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d.setdefault(400,"Vidya"))
print(d)
print(d.setdefault(100,"Raina"))
print(d)"""

#12)update()
"""x={}
d={100:"Bharath",200:"Kumar",300:"Reddy"}
print(d.update(x))"""

#No of occurences of each letter present in given string
"""word=input("Enter String...")
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
 print(k,"occured",v,"times")"""

#Dictionary Comprehension
"""squares={x:x*x for x in range(1,6)}
print(squares)
doubles={x:2*x for x in range(1,6)}
print(doubles)"""

d={
    "Bharath":9988776655,
    "Kumar":9900889988,
    "Reddy":6677889955
}
print(d)
print(d.get('Kumar'))
print(d.items())
d['Reddy']=9911223344
print(d)





