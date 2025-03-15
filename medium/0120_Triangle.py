class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(triangle[i]))] for i in range(len(triangle))]
       
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = min(dp[i][j], triangle[i][j] + dp[i - 1][j])
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = min(dp[i][j], triangle[i][j] + dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(triangle[i][j] + dp[i - 1][j - 1], triangle[i][j] + dp[i - 1][j])
                
        return min(dp[len(triangle) - 1])
