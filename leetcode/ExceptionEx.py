def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input types. Both arguments must be numbers.")
    else:
        print(f"Result: {result}")
    finally:
        print("Division operation completed.")

#divide(10, 2)
#divide(10, 0)
divide("10", 2) # Both should be int values