# Python program to find upper and lower case characters

"""def string_test(s):
    d={'Upper_case':0,'Lower_case':0}
    for i in s:
        if i.islower():
            d['Lower_case']+=1
        elif i.isupper():
            d['Upper_case']+=1
        else:
            pass
    print("Upper case letters:",d['Upper_case'])
    print("Lower case letters:", d['Lower_case'])
string_test("This is Dextris Company")"""


def string_test(s):
    upper=0
    lower=0
    for i in s:
        if i.islower():
            lower=lower+1
        elif i.isupper():
            upper=upper+1
        else:
            pass
    print("Upper case letters:",upper)
    print("Lower case letters:", lower)
string_test("This is Dextris Company")