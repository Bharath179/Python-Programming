def merge_alternately(a, b):
    i = j = 0
    result = ""

    while i < len(a) and j < len(b):
        result += a[i] + b[j]
        i += 1
        j += 1

    while i < len(a):
        result += a[i]
        i += 1

    while j < len(b):
        result += b[j]
        j += 1

    return result
print(merge_alternately("ravi", "reja"))