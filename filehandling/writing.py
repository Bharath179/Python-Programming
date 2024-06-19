#file=open('C:\\Users\\Lenovo\\Desktop\\Demo\\myFile.txt','w')   # open file for writing
#file.write('This is my first file\n')
#file.write('This is my second file\n')
#file.close()


#Reading all the data at once

#file=open('C:\\Users\\Lenovo\\Desktop\\Demo\\myFile.txt','r')
#print(file.read(6))  # Read given no of characters from the file
#print(file.read())  # Read entire content of file at once
#file.close()

#file=open('C:\\Users\\Lenovo\\Desktop\\Demo\\myFile.txt','r')
#print(file.readlines())  # Read entire content of file at once in array format
#file.close()

file=open('C:\\Users\\Lenovo\\Desktop\\Demo\\myFile.txt','r')
file.seek(4)
print(file.readline())  # Read the first line
#print(file.tell())
#file.close()


"""file=open('C:\\Users\\Lenovo\\Desktop\\Demo\\myFile.txt','a')
file.write("This is my third file\n")
file.close()"""

"""file=open('C:\\Users\\Lenovo\\Desktop\\Demo\\myFile.txt','r')
for l in file:
    print(l)
file.close()"""


