def common_letters():
    str1=input("Enter first string...")
    str2=input("Enter second string...")
    s1=set(str1)
    s2=set(str2)
    lst=s1 & s2    # & operator is to extracting common letter b/w two strings
    print(lst)

common_letters()