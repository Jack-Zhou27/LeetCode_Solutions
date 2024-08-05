class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while(i < len(nums)):
            start = i
            end = i
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
                end = i
            if start == end:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start]) + "->" + str(nums[end]))
            i += 1
        return ans
