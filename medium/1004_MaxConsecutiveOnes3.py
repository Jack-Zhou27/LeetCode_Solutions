class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        ans = 0
        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                #keep on updating left until we encounter a 0
                while l < len(nums) and nums[l] == 1:
                    l += 1
                k += 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
