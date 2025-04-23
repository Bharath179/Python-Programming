# Python program to find length of string

"""def Demo():
    s="Bharath"
    print(len(s))
Demo()"""

"""def string_length(str1):
    count=0
    for _ in str1:
        count=count+1
    return count
s = "kumar"
print(string_length(s))


def string_length(str1):
    count = 0
    for _ in str1:  # _ is used because we don't need the actual characters
        count += 1
    return count

# Take input from the user
user_input = input("Enter a string: ")

# Call the function and print the result
print("The length of the string is:", string_length(user_input))
"""

"""import os

# File path to create
file_path = 'C://Users//Lenovo//Desktop//example.txt'

# Open the file with the 'O_CREAT' and 'O_WRONLY' flags
# 'O_CREAT' means to create the file if it doesn't exist
# 'O_WRONLY' means open the file for writing
fd = os.open(file_path, os.O_APPEND | os.O_WRONLY)

# Data to write to the file (must be in bytes)
#data = "This is a sample text written using os module file descriptors.".encode()
data = "\nThis is additional text that will be appended.".encode()

# Write data to the file
os.write(fd, data)

# Close the file descriptor
os.close(fd)

print(f"File '{file_path}' created and data appended.")"""

'''data="All students are stupids"
f=open("abc.txt","w")
f.write(data)
with open("abc.txt","r+") as f:
     text=f.read()
     print(text)
     print("The Current Cursor Position: ",f.tell())
     f.seek(17)
     print("The Current Cursor Position: ",f.tell())
     f.write("Gems!!!")
     f.seek(0)
     text=f.read()
     print("Data After Modification:")
     print(text)'''


"""from zipfile import *
f=ZipFile('files.zip','w',ZIP_DEFLATED)
f.write('abc.txt')
f.close()
print("files.zip file created successfully")

try:
    with ZipFile('files.zip', 'r', ZIP_STORED) as f:
        names = f.namelist()  # List all the file names in the zip
        for name in names:
            print("Name is", name)
except FileNotFoundError:
    print("The file 'files.zip' does not exist. Please make sure the file is created.")"""

def number_to_string(num):
    return str(num)
print(type(number_to_string(123)))


