def count(str1, str2):
    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Initialize a counter variable to 0.
    counter = 0

    for char in str2:
        if char in char_count and char_count[char] > 0:
            counter += 1
            char_count[char] -= 1

    print("No. of matching characters are: " + str(counter))

# Driver code
if __name__ == "__main__":
    # Define two strings to compare.
    str1 = 'Bharath'
    str2 = 'kumar'

    # Call the count function with the two strings.
    count(str1, str2)
