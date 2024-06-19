class Parent:
    def display(self):

        print("Hi I am a parent...")

class child(Parent):
    def show(self):

        print("My favorite game is Vollyball...")
obj=child()
print(obj.display())
print(obj.show())
