"""def squares():
    s=[x*x for x in range(1,30)]
    print(s[:5])
    print(s[-5:])
squares()"""

'''def printValues():
    # Create an empty list 'l'
    l = list()
    # Loop from 1 to 30 (inclusive)
    for i in range(1, 30):
        # Calculate the square of 'i' and append it to the list 'l'
        l.append(i**2)
    # Print the first 5 elements of the list 'l'
    print(l[:5])
    # Print the last 5 elements of the list 'l'
    print(l[-5:])

# Call the printValues function to execute it
printValues()'''

"""l=[x*x for x in range(10000000000000000)]
print(l[0])"""

g=(x*x for x in range(10000000000000000))
print(next(g))
