class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        def bin_search(spell): #finds index of potion with smallest strength 
            l = 0 
            r = n - 1
            while l <= r:
                m = l + (r - l) // 2
                strength = potions[m] * spell
                if strength < success:
                    l = m + 1
                elif strength >= success:
                    r = m - 1
            return l
        
        ans = []
        for spell in spells:
            ans.append(n - bin_search(spell))
        return ans
