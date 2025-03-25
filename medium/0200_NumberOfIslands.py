class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #init
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(start_pt):
            fringe = [(start_pt[0], start_pt[1])]
            offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while fringe:
                x, y = fringe.pop(0)

                if visited[x][y] == 0 and grid[x][y] == '1':
                    visited[x][y] = 1

                    for offset in offsets:
                        dx = offset[0]
                        dy = offset[1]
                        nextX = x + dx
                        nextY = y + dy

                        if 0 <= nextX < m and 0 <= nextY < n and visited[nextX][nextY] == 0 and grid[nextX][nextY] == '1':
                            fringe.append((nextX, nextY))

                        
        #algo
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    ans += 1
                    dfs((i, j))
        return ans


