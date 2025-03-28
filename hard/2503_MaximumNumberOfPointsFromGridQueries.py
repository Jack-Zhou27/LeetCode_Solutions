class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        #init
        m = len(grid)
        n = len(grid[0])

        sorted_queries = [] #contains tuple, (query[index], index)
        for i in range(len(queries)):
            sorted_queries.append((queries[i], i))
        sorted_queries.sort(key=lambda x: x[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(cutoff): 
            ans = 0
            while fringe and fringe[0][0] < cutoff:
                
                val, x, y = heappop(fringe)
                ans += 1

                for dirr in directions:
                    dx = dirr[0]
                    dy = dirr[1]

                    next_x = x + dx
                    next_y = y + dy

                    if 0 <= next_x < m and 0 <= next_y < n:
                        if (next_x, next_y) not in visited:
                            heappush(fringe, (grid[next_x][next_y], next_x, next_y))
                            visited.add((next_x,next_y))
            return ans
        
        #algo
        fringe = [(grid[0][0], 0,0)] #minheap (grid[x][y], x, y)

        #NOTE FOR THE FUTURE:
        """
            set((0,0)) creates a set with two elements: {0, 0}, 
            because the parentheses in (0,0) create a tuple that gets 
            unpacked when passed to set().

            Thus, you must pass set([(0,0)]) instead of passing set((0,0))
        """
        visited = set([(0,0)]) 

        ans = [0 for _ in range(len(queries))]
        prev = 0
        for query in sorted_queries:
            cutoff = query[0]
            index = query[1] 

            curr = bfs(cutoff)
            ans[index] = (curr + prev)
            prev = ans[index]
        return ans
        


