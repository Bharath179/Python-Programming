"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,erno,esal):
        super().__init__(name,age)
        self.erno=erno
        self.esal=esal

    def diplay(self):
        print("The name of employee:",self.name)
        print("The age of employee:", self.age)
        print("The ID number of employee:", self.erno)
        print("The salary of employee:", self.esal)

e1=Employee('Bharath',27,'DEXIT0117',15000)
e1.diplay()
print("------------------------------------------")
e2=Employee('Vidya',27,'DEXIT0018',20000)
e2.diplay()"""

# Example for method overriding
class Parent:
    def job_profile(self):
        print("I am a Teacher")

class Child(Parent):
    def job_profile(self):
        super().job_profile()
        print("I am working as Quality Analyst")

c1=Child()
c1.job_profile()