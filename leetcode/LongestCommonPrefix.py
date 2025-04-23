def longest_common_prefix(strs):
    if not strs:
        return ""

    # Find the minimum length string from the array
    min_length = min(len(s) for s in strs)

    # Initialize the longest common prefix as an empty string
    lcp = ""

    # Compare characters of each string at each index up to the length of the shortest string
    for i in range(min_length):
        # Take the current character from the first string
        current_char = strs[0][i]

        # Check if this character is present at the same index in all strings
        if all(s[i] == current_char for s in strs):
            lcp += current_char
        else:
            break

    return lcp

# Example usage
strings = ["fly", "flower", "flight"]
print(longest_common_prefix(strings))
