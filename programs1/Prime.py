# Defining a Function
def isPrime(num):
    # Checking if num > 1 because there are no prime numbers less than 1
    if (num > 1):
        # Looping through the elements in a range of 2,num to find factors
        for i in range(2, num):
            if (num % i == 0):
                # Return False in Flag i.e not a prime number
                flag = False
                # End the Loop
                break
        else:
            # If there is no factor other than 1 return True in Flag
            flag = True
    return flag


# Sample input
num = 7
# Check if the flag is True or False
if (isPrime(num)):
    # If Flag is True print
    print("It is a Prime Number")
else:
    # If Flag is False print
    print("It is a not a Prime Number")