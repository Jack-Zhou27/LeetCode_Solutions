class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        left = 0
        right = len(height) - 1
        while(left < right): 
            tempArea = min(height[left], height[right]) * (right - left)
            if(tempArea > max):
                max = tempArea
            
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return max

