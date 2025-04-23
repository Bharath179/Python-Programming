class Mathmatics():
    def addition(self,a,b):
        return a+b

class Addition(Mathmatics):
    def addition(self,a,b):
        result=super().addition(a,b)
        print("Calling addition method from mathematics class using super call",result)
        return a+b

def perform_addition(math_obj,a,b):
    return math_obj.addition(a,b)

addition=Addition()
print("Using Addition object:", perform_addition(addition, 5, 3))
