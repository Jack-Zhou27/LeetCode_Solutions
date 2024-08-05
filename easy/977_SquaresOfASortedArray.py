class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                ans.append(nums[right] * nums[right])
                right -= 1
            else:
                ans.append(nums[left] * nums[left])
                left += 1
        return reversed(ans)
