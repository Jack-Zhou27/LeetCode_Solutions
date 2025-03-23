class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        def dijkstras(start):
            #init
            # visited = set()
            num_paths = [0 for i in range(n)]
            num_paths[0] = 1

            costs = [float('inf') for i in range(n)]
            costs[0] = 0
            minHeap = [(0, start)] #(cost, node) as minheap is based on lowest cost!

            paths = defaultdict(list)
            for a, b, c in roads:
                paths[a].append((c, b))
                paths[b].append((c, a))

            #algo
            while len(minHeap) > 0:
                cost, node = heappop(minHeap)

                if cost > costs[node]:
                    continue

                # if node not in visited:
                #     visited.add(node)

                for c, destination in paths[node]:
                    currCost = cost + c

                    if currCost < costs[destination]:
                        costs[destination] = currCost
                        num_paths[destination] = num_paths[node]
                        heappush(minHeap, (currCost, destination))

                    elif currCost == costs[destination]:
                        num_paths[destination] = (num_paths[node] + num_paths[destination]) % (10**9 + 7)

            return num_paths[n-1]

        return dijkstras(0)
            


