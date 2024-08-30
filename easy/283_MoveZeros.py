class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = 0
        while i < n:
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
                j -= 1
            i += 1
            j += 1
        
        
