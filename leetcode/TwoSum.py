'''def twoSum(nums,target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 1]

nums=[2,7,11,15]
target=9
print(twoSum(nums,target))'''


"""def twosum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<=right:
        if arr[left]+arr[right]>sum:
            right=right-1
        elif arr[left]+arr[right]<sum:
            left=left+1
        elif arr[left]+arr[right]==sum:
            print("Values of pair is",arr[left],"&",arr[right])
            right = right - 1
            left = left + 1
arr=[2,7,11,15]
sum=26
twosum(arr,sum)"""


# Input string
input_string = "python programming @123, abc, and, xyz"

# Split the string into words
words = input_string.split()

# Find the position of '@' symbol or '@123' in the words
start_index = next(i for i, word in enumerate(words) if word.startswith('@'))

# Slice the list of words starting from '@123' onward
filtered_words = words[start_index:]

# Join the filtered words back into a string with commas
output_string = "".join(filtered_words)
print(output_string)  # Output: "@123,abc,and,xyz"


