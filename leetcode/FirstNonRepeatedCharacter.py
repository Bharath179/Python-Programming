def first_non_repeating(str):
    dict={}
    size=len(str)
    for i in range(size):
        key=str[i]
        if key not in dict:
            dict[key]=1
        else:
            dict[key]=dict[key]+1
    counter = 0
    for idx in range(len(str)):
        if (dict[str[idx]] == 1):
             return str[idx],counter
        counter=counter+1
print(first_non_repeating("ABABDGD"))

'''for key,value in dict.items():
     if value==1:
       print(key,value)
        break'''
