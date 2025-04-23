'''def add(*args):
    c=0
    for i in args:
        c=c+i
    print(f"The sum is {c}")
add(2,3,4)'''

'''def Person(name,age=27):
    print(f"The name of person is {name}.")
    print(f"The age of Bharath is {age}.")
Person("Bharath")'''

'''def multiply(**kwargs):
    for key,value in kwargs.items():
     print(key,value)
multiply(a=2,b=6,c=3)'''


'''# Python code to demonstrate the use of variable-length arguments
# Defining a function
def function(*args_list):
    ans = []
    for l in args_list:
        ans.append(l.upper())
    return ans

# Passing args arguments
object = function('Python', 'Functions', 'tutorial')
print(object)'''


'''# defining a function
def function(**kargs_list):
    ans = []
    for key, value in kargs_list.items():
        ans.append([key, value])
    return ans

# Paasing kwargs arguments
object = function(First="Python", Second="Functions", Third="Tutorial")
print(object)'''


'''# Python code to demonstrate the use of return statements
# Defining a function with return statement
def square(num):
    return num ** 2

# Calling function and passing arguments.
print("With return statement")
print(square(52))'''


'''# Defining a function without return statement
def square(num):
    num ** 2

# Calling function and passing arguments.
print("Without return statement")
print(square(52))'''

'''class Student:
    id = 101
    name = "Bharath"
    email = "bharath@abc.com"
# Declaring function
    def getinfo(self):
        print(self.id, self.name, self.email)
s = Student()
s.getinfo()'''
'''delattr(Student,'course') # Removing attribute which is not available  
s.getinfo() # error: throws an error '''




