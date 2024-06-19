def freq_words():
    str=input("Enter a string...")
    li=str.split()
    d={}

    for i in li:
        if i not in d.keys():     #d[i]=d.get(i,0)+1
         d[i]=0
        d[i]=d[i]+1
    print(d)
freq_words()