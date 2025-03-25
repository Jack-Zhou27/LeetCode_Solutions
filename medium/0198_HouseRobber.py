class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        largest_till = [nums[0], max(nums[0], nums[1])]
        prev1, prev2 = max(nums[0], nums[1]), nums[0]
        
        for i in range(2, len(nums)):
            largest_till.append(max(prev2 + nums[i], prev1))
            prev2 = prev1
            prev1 = largest_till[-1]

        return largest_till[-1]
