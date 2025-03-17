class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        #init
        n = len(isConnected)
        visited = set()

        #algo
        def dfs(city):
            for neighbors in range(n):
                if isConnected[city][neighbors] == 1 and neighbors not in visited:
                    visited.add(neighbors)
                    dfs(neighbors)
        
        ans = 0
        for city in range(n):
            if city not in visited:
                ans += 1
                dfs(city)
        return ans
        

