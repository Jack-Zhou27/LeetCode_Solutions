class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #check base case
        if(s == ""):
            return True

        #algorithm
        currIndex = 0
        for c in s:
            while(currIndex < len(t) and t[currIndex:currIndex + 1] != c):
                currIndex += 1
            currIndex += 1
        
        if(currIndex <= len(t)):
            return True
        return False



        """
        This code below assumes that we DO NOT consider relative positions of the characters

        frequencyListT = {key: t.count(key) for key in t}
        for c in s:
            if(c not in frequencyListT or frequencyListT[c] < 0):
                return False
            frequencyListT[c] = frequencyListT[c] - 1
        
        return True
        """



        
