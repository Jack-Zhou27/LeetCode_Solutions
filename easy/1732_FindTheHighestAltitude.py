class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_al = 0
        previous = 0
        for r in range(0,len(gain)):
            previous += gain[r]
            max_al = max(previous,max_al)
        return max_al
