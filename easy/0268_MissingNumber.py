class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        currSum = 0
        maxSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum += (i + 1)
            
        return maxSum - currSum
