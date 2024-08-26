class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        array = []
        for c in s:
            if c in array:
                ans = max(ans, len(array))
                while array.pop(0) != c:
                    pass
            array.append(c)
            
        
        return max(ans, len(array))
               










