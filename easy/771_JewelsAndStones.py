class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        frequencyList = {key: stones.count(key) for key in stones}
        ans = 0
        for c in jewels:
           if c in frequencyList:
                ans += frequencyList[c]
        return ans
