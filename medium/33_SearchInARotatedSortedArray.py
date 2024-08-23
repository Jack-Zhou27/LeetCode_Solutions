class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            #does target exist in left half?
            #yes
            elif nums[l] <= nums[m] and nums[l] <= target < nums[m]:
                r = m - 1
            #no
            elif nums[l] <= nums[m] and not nums[l] <= target < nums[m]:
                l = m + 1
            
            #does target exist in right half
            #yes
            elif nums[r] >= nums[m] and nums[m] < target <= nums[r]:
                l = m + 1
            #no
            elif nums[r] >= nums[m] and not nums[m] < target <= nums[r]:
                r = m - 1
        return -1
