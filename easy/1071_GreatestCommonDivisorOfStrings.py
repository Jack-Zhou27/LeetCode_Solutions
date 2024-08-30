class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        #finds if s1 successfully divide str1 -> big1 and str2 -> big2 
        def divides(s1, big1, big2):
            if len(big2) % len(s1) != 0 or len(big1) % len(s1):
                return ""
            
            i = 0
            while i < len(big2):
                if big2[i : i + len(s1)] != s1:
                    return ""
                i += len(s1)
            
            i = 0
            while i < len(big1):
                if big1[i : i + len(s1)] != s1:
                    return ""
                i += len(s1)

            return s1

        #assign s1 as the shorter string and s2 as the longer string
        s1 = ""
        s2 = ""
        if len(str1) < len(str2):
            s1 = str1
            big1 = str1
            s2 = str2
            big2 = str2
        else:
            s1 = str2
            big1 = str2
            s2 = str1
            big2 = str1

        #algorithm 
        i = len(s1)
        ans = ""
        while ans == "" and i > 0:
            s1 = s1[0: i]
            ans = divides(s1, big1, big2)
            i -= 1
            
        return ans
