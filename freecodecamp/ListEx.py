'''students=['Bharath','Sweaty','Vidya']
for student in students:
    print(student)
for i in range(len(students)):
    print(i+1,students[i])'''


#Dictionary
'''students={
    'Bharath':'Kambalapalli',
    'Sweaty':'Bangalore',
    'Vidya':'Gulbarga'
}
for student in students:
    print(student,students[student],sep=':')'''
#print(students['Bharath'])

'''students=[
    {'name':'Hermione','house':'Gryffindor','patronus':'Otter'},
    {'name':'Harry','house':'Gryffindor','patronus':'Stag'},
    {'name':'Ron','house':'Gryffindor','patronus':'Jack Russell terrier'},
    {'name':'Draco','house':'Slytherin','patronus':'None'}
]
for student in students:
    print(student['name'],student['house'],student['patronus'],sep=':')
    #print(student)'''

'''def main():
    print_column(3)
def print_column(n):
    print("#\n"*n,end='')
for _ in range(n):
     print('#')
main()'''

def main():
    print_square(3)
def print_square(n):
    for i in range(n):
        #print("#"*n)
        for j in range(n):
            print("#",end="")
        print()
main()