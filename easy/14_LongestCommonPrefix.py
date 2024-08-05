class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
       smallest = 201
       smallestString = ""
       for s in strs:
            if(len(s) < smallest):
                smallest = len(s)
                smallestString = s
        
       ans = ""
       for i in range (0, smallest):
            for j in range(0, len(strs)):
                temp = strs[j]
                if(temp[i : i + 1] != smallestString[i : i + 1]):
                    return ans
            ans += smallestString[i : i + 1]
       return ans

        
