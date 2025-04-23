# The original input string
#OriginalString = "The quick brown fox jumps over the lazy dog."
OriginalString = "ABCABCABBCDE"

# Splitting the string and removing spaces and punctuation.
CleanedString = ''.join(filter(lambda x: x.isalpha() or x.isspace() or x.isdigit(), OriginalString.split()))

# To Bring Consistency in the string, converting everything to lowercase
CleanedString = CleanedString.upper()

# dictionary comprehension for the frequency count;
result = {x: CleanedString.count(x) for x in CleanedString}

# Printing the result dictionary
print(result)


