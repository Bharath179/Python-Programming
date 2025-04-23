import os
#print(os.getcwd()) # To get the current working directory

'''os.chdir("C:\\Users\\Lenovo\\Documents") # To change current directory to another directory
print(os.getcwd())'''

'''os.chdir("C:\\Users")
print(os.listdir()) # To get files present in subdirectory'''

'''os.chdir("C:\\Users\\Lenovo\\Documents\\Custom Office Templates")
os.mkdir("test")'''  # To create sub Directory

'''os.chdir("C:\\Users\\Lenovo\\Documents\\Custom Office Templates")
os.renames("test","test1") # It is use to rename existing directory  
print("Rename is sucessfull")'''

'''os.chdir("C:\\Users\\Lenovo\\Documents\\Custom Office Templates")
os.rmdir("test1") # To remove sub directory
print("Sucessfully removed directory")'''

os.chdir("C:\\Users\\Lenovo\\Documents")
os.remove("C:\\Users\\Lenovo\\Documents\\BEI605- Embedded-System.pdf") # To remove file
print("Sucessfully removed file")





