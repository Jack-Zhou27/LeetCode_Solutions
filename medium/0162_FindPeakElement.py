class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        #bin_search
        l = 0 
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            
            #is peak
            #edge cases
            if m + 1 >= len(nums):
                if nums[m - 1] < nums[m]:
                    return m
                else:
                    r = m - 1
            elif m - 1 < 0:
                if nums[m] > nums[m + 1]:
                    return m
                else:
                    l = m + 1

            #standard case
            elif nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            
            elif nums[m - 1] < nums[m] < nums[m + 1]: #is ascending to the right
                l = m + 1
            
            elif nums[m - 1] > nums[m] > nums[m + 1]: #is descending to the right
                r = m - 1
            else: #is valley
                l += 1

        return l


