"""with open("demo.txt",'w') as file:
    data=file.write("File handling is essential for working with data in Python. "
               "You can open files in different modes, read/write/append data,"
               " and ensure that files are automatically closed using the with statement."
               " Always ensure to handle errors gracefully, especially when working with file I/O operations.")
print(data)"""

"""with open("demo.txt",'r') as file:
    file.seek(10)
    content=file.read()
    print(content)"""

with open("demo.txt",'r') as file:
    content=file.read()
    word_replace=content.replace('closed','open')
    print(word_replace)