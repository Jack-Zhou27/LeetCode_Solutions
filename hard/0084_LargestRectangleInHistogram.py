class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = -1
        stack = []

        #Create a monotonic stack where we pop the current bar if the bar after it is lower as we cannot extend the height of the current bar to the right and still create a rectangle
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                ans = max(ans, height * (i - index))
                start = index
            stack.append((start, heights[i]))
        
        #handle the remaining montonic increasing stack
        while stack:
            ans = max(ans, (len(heights) - stack[-1][0]) * stack[-1][1])
            stack.pop()

        return ans
            
                
