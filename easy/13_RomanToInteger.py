class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        ans = 0
        for i in range (0, len(s)):
            if(i + 1 < len(s) and map[s[i : i + 1]] < map[s[i + 1 : i + 2]]):
                ans -= map[s[i : i + 1]]
                continue
            ans += map[s[i : i + 1]]
        
        return ans
            
