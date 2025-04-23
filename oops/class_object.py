class Animal:
    def __init__(self,name,color,):
        self.name = name
        self.color = color

    # Method to display Animal details
    def display_info(self):
        print(f"The name of animal",{self.name},"and color is",{self.color})

# creating object(instance) of the class Animal

animal=Animal('Tiger','Black with dark orange')

# Accessing object attributes and calling method
animal.display_info()
