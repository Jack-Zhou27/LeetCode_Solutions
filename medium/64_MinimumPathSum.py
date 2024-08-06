class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
               if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i - 1][j])
               if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j - 1])
        
        return dp[m - 1][n - 1]
