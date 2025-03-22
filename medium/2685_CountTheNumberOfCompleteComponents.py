class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(v, arr):
            if v in visited:
                return
            
            arr.append(v)
            visited.add(v)
            for neighbor in adj[v]:
                dfs(neighbor, arr)
            return arr
        
        #init
        adj = defaultdict(list)
        visited = set()
        for arr in edges: #this adj list ensures each node is connected to each other node! 
            adj[arr[0]].append(arr[1])
            adj[arr[1]].append(arr[0])
            

        #algo
        ans = 0
        for v in range(n):
            if v in visited:
                continue
            components = dfs(v, [])
            if all([len(adj[node]) == len(components) - 1 for node in components]):
                ans += 1
        return ans


        
