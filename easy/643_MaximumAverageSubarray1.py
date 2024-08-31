class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        #intialize temp
        temp = 0
        for i in range(0, k):
            temp += nums[i] 
        temp /= k

        #algorithm
        ans = temp
        i = k
        while i < len(nums):
            temp += (nums[i] - nums[i - k]) / k
            ans = max(ans, temp)
            i += 1

        return ans
