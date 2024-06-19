
'''def twosum(nums, target):
        left=0
        right=len(nums)-1
        while left<right:
            total=nums[left]+nums[right]
            if total==target:
                return [left+1,right+1]
            elif total>target:
                right-=1
            else:
                left+=1
nums=[2,7,11,15]
target=22
print(twosum(nums,target))'''

"""a=[2,7,11,15]
target=22
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
         print([i,j])"""

import random
import string
def generate_password(length=8):
    # Define the character set to generate the password from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


# Example usage:
generated_password = generate_password()
print("Generated Password:", generated_password)



