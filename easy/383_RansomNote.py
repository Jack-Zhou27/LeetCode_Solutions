class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequencyList = {key: magazine.count(key) for key in magazine}

        for c in ransomNote:
            if c not in frequencyList or frequencyList[c] <= 0:
                return False
            else:
                frequencyList[c] -= 1
        return True

        
