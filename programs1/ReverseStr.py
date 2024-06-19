
def reverseString(x):
    # Declaring an empty String
    NewString = ""
    # Traversing through individual characters in a string
    for i in x:
        # Add the character to the empty string
        NewString = i + NewString
    # return the new string
    return NewString
# Sample String
string = "Dextris Software Solutions"
# Function Call
ReversedString = reverseString(string)
# Printing Output
print(ReversedString)

#H e l l o
#H
#e H
#l e H
#l l e H
#o l l e H

