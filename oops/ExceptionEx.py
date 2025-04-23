# Function to perform division
def divide(a, b):
    return a / b

# Get input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the division and print the result
    result = divide(num1, num2)
    print(f"The result of {num1} divided by {num2} is {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
