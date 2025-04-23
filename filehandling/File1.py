
'''f=open('abc.txt','r')
print('Name',f.name)
print('Mode',f.mode)
print('Closed',f.closed)
print('Is Readable',f.readable())
print('Is Writable',f.writable())
f.close()
print('Closed',f.closed)'''

'''f=open('C:\\Users\\Lenovo\\Desktop\\abc.txt','w')
f.write('Welcome\n')
f.write('To\n')
f.write('Bangalore\n')
print("Data written to file successfully")
f.close()'''

'''f=open('C:\\Users\\Lenovo\\Desktop\\abc.txt','a')
f.write('Hi\n')
print("Data written to file successfully")
f.close()'''

'''f=open('C:\\Users\\Lenovo\\Desktop\\abc.txt','w')
list=['Hi ','Bharath ','Welcome ','To ','Dextris']
f.writelines(list)
print("Data written to file successfully")
f.close()'''

'''f1=open('abc.txt','r')
f2=open('abc1.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print("Data copied successfully")'''

import os
fname=input('Enter File Name...')
if os.path.isfile(fname):
    print('File Exists...',fname)
    print('The content of file is...')
    f=open(fname,'r')
    print('*'*40)
    text=f.read()
    print(text)
    print('*' * 40)
else:
    print("File does'nt exists",fname)

