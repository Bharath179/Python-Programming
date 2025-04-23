occurence=input("Enter String...")
dict={}
for i in occurence:
    dict[i]=dict.get(i,0)+1
for k,v in dict.items():
    print(k,"occured",v,"times")