class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mostCandy = 0
        for i in candies:
            if i > mostCandy:
                mostCandy = i
        
        ans = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mostCandy:
                ans.append(True)
            else:
                ans.append(False)

        return ans
