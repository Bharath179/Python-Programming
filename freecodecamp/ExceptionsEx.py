'''try:
     x=int(input("What's x is? "))
     print(f"x is {x}")
except ValueError:
     print("x must be integer value")'''


'''try:
    x=int(input("What's x is? "))
except ValueError:
    print("x must be integer value")
else:
    print(f"x is {x}")'''

'''def main():
    x=get_int()
    print(f"x is {x}")
def get_int():
    while True:
       try:
          x=int(input("What's x is? "))
          #break
       except ValueError:
          print("x must be integer value")
       else:
           break
    return x
main()'''


'''def main():
    x=get_int()
    print(f"x is {x}")
def get_int():
    while True:
       try:
          return int(input("What's x is? "))
       except ValueError:
          print("x must be integer value")
       
main()'''

def main():
    x = get_int("What's x is? ")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()

