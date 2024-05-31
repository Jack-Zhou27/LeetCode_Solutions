class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        #greedy algorithm
        buyin = prices[0]
        for i in prices:
            if(i - buyin < 0):
                buyin = i
            else:
                ans = max(ans, i - buyin)

        return ans
