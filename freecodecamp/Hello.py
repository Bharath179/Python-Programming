'''name=input("What's your name? ").strip().title()

print(f"hello, {name}")'''

'''x=input("Enter the value of x:")
y=input("Enter the value of x:")

z=int(x)+int(y)
print(z)'''

'''x=float(input("Enter the value of x:"))
y=float(input("Enter the value of x:"))

z=round(x+y)
print(f"{z:.2f}")'''


'''def main():
    x=int(input("Enter number:"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2==0 else False
main()'''

'''if n%2==0:
        return True
    else:
        return False'''

#main()

name=input("Enter Name:")

match name:
    case "Bharath":
        print("Python Test Engineer")
    case "Vidya":
        print("Reels Maker")
    case "Kumar":
        print("Java Test Engineer")
    case "AnushkaShetty":
        print("Film Actress")
    case _:
        print("Who are you")



