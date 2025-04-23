def index_of_first_occurence_in_string(haystack,needle):
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        match = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i

    return -1
print(index_of_first_occurence_in_string("sadbutsad","sad"))