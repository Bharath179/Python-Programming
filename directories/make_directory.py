import os

#os.mkdir("C:\\Users\\Lenovo\\Documents\\directory")
# os.makedirs("C:\\Users\\Lenovo\\Documents\\directory\\file\\file1")
#print("Directory has been created")

# To get current working directory

# cwd=os.getcwd()
# print("Current Working Directory:",cwd)

# Create subdirectory in the current working directory

# os.mkdir("mysub")
# print("mysub directory created in cwd")

# Create directory inside subdirectory

# os.mkdir("mysub/mysub2")
# print("mysub2 created inside mysub")

# Remove the mysub2 from mysub directory

# os.rmdir("mysub/mysub2")
# print("mysub2 directory deleted")

# To remove multiple subdirectories inside directory

# os.removedirs("sub1/sub2/sub3")
# print("All 3 directories sub1,sub2 and sub3 removed")

# To rename the directory

# os.rename("mysub","newdir")
# print("mysub directory renamed to newdir")

# os.rmdir("C:\\Users\\Lenovo\\Documents\\directory")
# print("Directory has been removed")

"""import shutil

# Remove a non-empty directory 'example_dir' and its contents
shutil.rmtree("newdir")
print("Directory 'newdir' and its contents have been deleted.")"""

"""if os.path.exists("C:\\Users\\Lenovo\\Documents\\directory"):
    print("Directory Exists")
else:
    print("Directory does not exists")"""

"""if os.path.isdir("C:\\Users\\Lenovo\\Documents\\directory"):
    print("It is a Directory")
else:
    print("It is not a Directory")"""

# list all files and directories in current working directory

# contents = os.listdir(".")
# print("Contents of the current directory:", contents)

# List contents of the current directory using os.scandir()

# with os.scandir('.') as entries:
#     for entry in entries:
#         print(entry.name)


# Change the current working directory to 'example_dir'
os.chdir("directory")
print("Current directory changed to 'directory'")

# Verify the current working directory
print("Current working directory:", os.getcwd())


