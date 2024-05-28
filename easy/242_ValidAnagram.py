class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:

        #this function converts a string into an array. ie) str -> 's', 't', 'r'
        def stringToArray(s):
            return [c for c in s]

        stemp = stringToArray(s)
        stemp.sort()

        ttemp = stringToArray(t)
        ttemp.sort()
        
        #if the two strings are different in length, then it cannot be an anagram
        if(len(ttemp) != len(stemp)):
            return False
        
        #if the two strings have different characters, then it cannot be an anagram
        for i in range(0, len(stemp)):
            if(stemp[i] != ttemp[i]):
                return False
        return True
    
        

    

        
