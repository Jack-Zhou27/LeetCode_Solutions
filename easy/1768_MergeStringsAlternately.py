class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        count = 0
        for c in word1:
            if(count >= len(word2)):
                ans += word1[count: len(word1)]
                break
            else:
                ans += c + word2[count: count + 1]
                count += 1
        if len(word2) > len(word1):
            ans += word2[len(word1): len(word2)]
        return ans
            
