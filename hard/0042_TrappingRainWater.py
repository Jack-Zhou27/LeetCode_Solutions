class Solution:
    def trap(self, height: List[int]) -> int:
        if(len(height) <= 2):
            return 0
    
        ans = 0
        left = [0] * len(height)
        left[0] = height[0]
        right = [0] * len(height)
        right[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])
            right[len(height) - 1 - i] = max(right[len(height) - i], height[len(height) - i - 1])
        
        for i in range(0, len(height)):
            ans += min(left[i], right[i]) - height[i]

        return ans

        










        """
        Failed Attempt 1: 

        ans = 0
        left = 0
        right = 1
        tempArea = 0
        while(left < len(height) - 1):
            if(right == len(height)):
                left += 1
                right = left + 1
                tempArea = 0
            elif(height[right] >= height[left]):
                ans += max(0, height[left] * (right - left - 1) - tempArea)
                tempArea = 0
                left = right
                right += 1
            else:
                tempArea += height[right]
                right += 1
        return ans
        """
