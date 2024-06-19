l1=['123Hello4','345World89','980Lion99']

def seperate_data(l1):
    num_list=[]
    word_list=[]
    for i in l1:
        num_data=""
        char_data=""
        for ch in i:
            if ch.isdigit():
                num_data=num_data+ch
            else:
                char_data=char_data+ch
        num_list.append(num_data)
        word_list.append(char_data)
    print(num_list)
    print(word_list)
seperate_data(l1)

