class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        prev = 0
        nextt = 0
        for index, n in enumerate(nums):
            if n > 0:
                if index > 0 and nums[index] == nums[index - 1]:
                    continue
                prev = nextt
                nextt += n - prev
                ans += 1
            if nextt >= nums[-1]:
                return ans
        return ans
