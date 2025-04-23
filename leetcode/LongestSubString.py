def longest_substring_without_repeating(s):
    # Initialize variables
    left = 0
    max_length = 0
    s1 = set()

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # Check if the current character is already in the set
        while s[right] in s1:
            # If yes, move the left pointer to the right
            s1.remove(s[left])
            left += 1

        # Add the current character to the set
        s1.add(s[right])

        # Update the maximum length found
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
input_str = "abcabcbb"
print("Longest substring without repeating characters:",
      longest_substring_without_repeating(input_str))

input_str = "bbbbb"
print("Longest substring without repeating characters:",
      longest_substring_without_repeating(input_str))

input_str = "pwwkew"
print("Longest substring without repeating characters:",
      longest_substring_without_repeating(input_str))

'''arr = [18, 18, 18, 6, 3, 4, 9, 9, 9]
# size of the list
size = len(arr)

# looping till length - 2
for i in range(size-2):

    # checking the conditions
    if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
        # printing the element as the
        # conditions are satisfied
        print(arr[i])'''
