class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        def isVowel(c):
            if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
                return True
            return False

        def numOfVowels(s):
            count = 0
            for c in s:
                if isVowel(c):
                    count += 1
            return count
    
        temp = numOfVowels(s[0 : k])
        ans = temp
        i = k
        while i < len(s):
            if isVowel(s[i : i + 1]):
                temp += 1
            if isVowel(s[i - k: i - k + 1]):
                temp -= 1
            ans = max(ans, temp)
            i += 1

        return ans
