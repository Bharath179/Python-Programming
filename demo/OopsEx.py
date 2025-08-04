# custom exception
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age cannot be less than 18"):
        self.age = age  # Store the invalid age
        self.message = message  # Default error message
        super().__init__(self.message)  # Call the base class constructor with the error message

    def __str__(self):
        return f"{self.message}: {self.age}"


class Person:
    def __init__(self, name, age):
        self.name = name  # Name of the person
        self.age = age  # Age of the person

    def validate_age(self):
        if self.age < 18:
            # Raise custom exception if age is less than 18
            raise InvalidAgeError(self.age)

    def display_info(self):
        print("Name: %s" % self.name)
        print("Age: %s" % self.age)


# Creating an object of Person class
person1 = Person("John", 17)

try:
    # Validating the person's age
    person1.validate_age()
except InvalidAgeError as exception:
    # Handling the custom exception
    print(f"Error: {exception}")
else:
    person1.display_info()  # If exception occurs this line will not get executed
