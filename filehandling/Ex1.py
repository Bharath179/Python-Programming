'''def read_file(file_name):
    with open(file_name,'r') as file:
     print(file.read())
read_file("The_file_does_not_exist.txt")'''

'''import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("A New request Came:")
try:
   x=int(input("Enter First Number: "))
   y=int(input("Enter Second Number: "))
   print(x/y)
except ZeroDivisionError as msg:
   print("cannot divide with zero")
   logging.exception(msg)
except ValueError as msg:
   print("Enter only int values")
   logging.exception(msg)
   logging.info("Request Processing Completed")'''

'''d={'swift':100,'BMW':200,'KIA':300}
d1=d.keys()
print(d1)
d1=input("Enter car name to get price:")
print(d.get(d1))'''

'''t=(10,20,30,40)
print(t[1:3])'''

file=open('knb.txt','w')
file.write("Hi my name is Bharath")
file.close()




