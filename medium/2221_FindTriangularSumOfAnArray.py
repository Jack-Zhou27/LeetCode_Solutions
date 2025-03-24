class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums
        for i in range(n - 1, 0, -1):
            nextt = []
            for j in range(1, len(prev)):
                nextt.append((prev[j] + prev[j - 1]) % 10)
            prev = nextt
        return prev[0]
