"""list=[1,2,3,4,5,6,7]
Sum=0
Sum=sum([x for x in list if x%2==0])
print(Sum)"""


# Defining a Function
def EvenOdd(Data):
    # Checking if the number is even
    print([x for x in Data if x % 2 == 0])
    # Checking if the number is odd
    print([x for x in Data if x % 2 != 0])


# Sample Data
Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Function Call
EvenOdd(Data)