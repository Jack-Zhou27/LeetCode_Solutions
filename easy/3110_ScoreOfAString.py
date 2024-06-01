class Solution:
    def scoreOfString(self, s: str) -> int:
        charArray = list(s)
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(charArray[i - 1]) - ord(charArray[i]))
        return ans
