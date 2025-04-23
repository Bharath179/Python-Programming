'''class Solution:
    def maxSubArray(nums):
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum

    if __name__ == "__main__":
        nums = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
        #nums=[1]
        print(maxSubArray(nums))'''

def maxSum_Subarray(arr):
    size=len(arr)
    cur_sum=0
    max_sum=arr[0]
    start=0;end=0;pos=0
    for i in range (0,size):
        cur_sum=cur_sum+arr[i]
        if max_sum<cur_sum:
            max_sum=cur_sum
            start=pos
            end=i
        if cur_sum<0:
            cur_sum=0
            pos=i+1
    print("Maximum sum subarray is",max_sum)
    print("Start index of window is",start)
    print("End index of window is",end)

arr=[4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
maxSum_Subarray(arr)
