
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
print(twoSum([2,7,11,15],22))


def lengthOfLongestSubstring(s):
    max_length = 0
    n = len(s)

    # Generate all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            # Check if the substring has all unique characters
            if len(set(substring)) == len(substring):
                max_length = max(max_length, len(substring))

    return max_length
print(lengthOfLongestSubstring("abcabcbb"))