'''i=3
while i!=0:
    print("Bharath")
    i=i-1'''

'''i=0
while i<3:
    print("AnushkaShetty")
    i+=1'''

'''while True:
    n=int(input("What's n? "))
    if n>0:
        break
for _ in range(n):
    print("Sweaty")'''

def main():
    number=get_number()
    sweet(number)
def get_number():
    while True:
        n=int(input("What's n? "))
        if n>0:
            break
    return n
def sweet(n):
    for _ in range(n):
        print("Sweaty")
main()