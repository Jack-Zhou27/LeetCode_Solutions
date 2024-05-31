class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        #greedy algorithm
        prev = prices[0]
        for i in range(0, len(prices)):
            if(prices[i] - prev > 0):
                ans += prices[i] - prev
            prev = prices[i]
        return ans
