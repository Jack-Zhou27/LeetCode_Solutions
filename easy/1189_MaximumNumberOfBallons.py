class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }
        
        for c in text:
            if c in map:
                map[c] += 1
        
        ans = 9999
        for key in map:
            if key == 'l' or key == 'o':
                ans = min(ans, map[key] // 2)
            else:
                ans = min(ans, map[key])
        return ans
