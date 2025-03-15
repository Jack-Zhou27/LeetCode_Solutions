class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        #init
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0), (0, 1), (-1,0), (0, -1)]
        freshOranges = 0
        fringe = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    fringe.append((i, j, 0))
                if grid[i][j] == 1:
                    freshOranges += 1
        
        #algorithm
        maxTime = 0
        while len(fringe) > 0:
            x, y, time = fringe.pop(0)
            maxTime = max(maxTime, time)

            for a, b in directions:
                nextX = x + a
                nextY = y + b

                if 0 <= nextX < m and 0 <= nextY < n and grid[nextX][nextY] == 1:
                    #visited
                    grid[nextX][nextY] = 2
                    freshOranges -= 1

                    fringe.append((nextX,nextY, time + 1))


        if freshOranges > 0:
            return -1
        return maxTime


                
