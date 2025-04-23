"""class Parent:
    def __init__(self,job,salary):
        self.job=job
        self.salary=salary

    def display(self):
        return "This is parent method"

    def __str__(self):
        return f"Parent(Job: {self.job}, Salary: {self.salary})"

class Child:
    def __init__(self,job,salary):
        self.job = job
        self.salary = salary

    def display(self):
        return "This is child method"

    def __str__(self):
        return f"Child(Job: {self.job}, Salary: {self.salary})"

parent=Parent('Vikram','10K')
child=Child('AalekyaReddy','20K')

for x in(parent,child):
    print(x.display())

print(parent)
print(child)
"""

class Animal:
    def speak(self):
        print("This is animal class")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("This is dog class")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("This is cat class")

dog=Dog()
cat=Cat()
dog.speak()
cat.speak()