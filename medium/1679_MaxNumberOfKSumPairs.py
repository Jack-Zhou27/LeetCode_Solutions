class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0
        while l < r:
            total = nums[l] + nums[r] 
            if total == k:
                l += 1
                r -= 1
                ans += 1
            elif total < k:
                l += 1
            else:
                r-= 1
        return ans
