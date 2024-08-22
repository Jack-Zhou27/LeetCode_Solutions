class Solution:
    def findMin(self, nums: List[int]) -> int:

        #binary search 
        ans = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            ans = min(ans, nums[m]) #this is the only addition we make to the classic binary search algorithm!!!
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return ans
        
        
                
