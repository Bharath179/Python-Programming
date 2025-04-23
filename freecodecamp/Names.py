'''names=[]

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello,{name}")'''

#name=input("What's your name? ")

'''file=open("names.txt",'a')
file.write(f"{name}\n")
file.close()'''

'''with open('names.txt','a') as file:
    file.write(f"{name}\n")'''


'''with open('names.txt','r') as file:
    lines=file.readlines()
for line in lines:
    print("hello",line.rstrip())'''

'''names=[]
with open('names.txt','r') as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names,reverse=True):
    print(f"hello,{name}")'''

'''with open('names.txt','r') as file:
    for line in sorted(file):
        print(f"hello,",line.rstrip())'''


with open('students.csv') as file:
    for line in file:
        
        name,age,country=line.rstrip().split(",")
        print(f"{name} age is {age} and he is from {country}")

'''import csv

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "age", "country"]

    writer.writerow(field)
    writer.writerow(["Bharath", "27", "Bangalore"])
    writer.writerow(["Kumar", "23", "Chintamani"])
    writer.writerow(["Reddy", "50", "Chikkabalapura"])'''


