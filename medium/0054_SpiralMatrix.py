class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #init
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        visitCount = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        x = 0
        y = 0

        def traverse_until_edge(x, y, dx, dy):
            nonlocal visitCount
            while 0 <= x < rows and 0 <= y < cols and visited[x][y] == False:
                visited[x][y] = True
                visitCount += 1
                ans.append(matrix[x][y])
                x += dx
                y += dy
            
            #reset x and y
            x -= dx
            y -= dy
            return x,y
        
        #algo
        iterations = 0
        while visitCount != rows * cols:
            if iterations % 4 == 0: #move right
                x,y = traverse_until_edge(x, y, 0, 1)
                x += 1
            elif iterations % 4 == 1: #move down
                x,y = traverse_until_edge(x, y, 1, 0)
                y -= 1
            elif iterations % 4 == 2: #move left
                x,y = traverse_until_edge(x, y, 0, -1)
                x -= 1
            else: #move up
                x,y = traverse_until_edge(x,y, -1, 0)
                y += 1
            iterations += 1
        return ans
