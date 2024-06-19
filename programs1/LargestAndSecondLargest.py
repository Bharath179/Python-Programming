def LargestAndSecondLargest(Data):
    # Sorting the list in Ascending Order
    Data = sorted(Data)
    # Extracting the last element (Largest Element)
    largestElement = Data[-1]
    # Extracting the second last element (Second Largest Element)
    SecondlargestElement = Data[-2]
    # Returning the variables containing the elements.
    return largestElement, SecondlargestElement


Data = [20, 15, 8, 12, 19]
print(LargestAndSecondLargest(Data))