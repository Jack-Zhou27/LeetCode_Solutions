class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        smallest = 2147483647
        ans = 0
        for i in nums:
            if abs(i) < smallest or (i > 0 and i <= smallest):
                smallest = abs(i)
                ans = i
        return ans
