class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVol(c):
            return(bool(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'))
            
        temp = list(s)
        vowels = []
        for c in temp:
            if(isVol(c)):
                vowels.append(c)
        
        n = 1
        ans = ""
        for c in temp:
            if(isVol(c)):
                ans += vowels[len(vowels) - n]
                n += 1
            else:
                ans += c
        return ans

       
