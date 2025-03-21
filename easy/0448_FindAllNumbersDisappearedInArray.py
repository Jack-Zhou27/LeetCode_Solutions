class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        visited = set()
        for i in range(len(nums)):
            visited.add(nums[i])
        
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in visited:
                ans.append(i)
        return ans
