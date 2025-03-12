class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        #init paths from city a to b
        #init all neighbors from city a
        paths = defaultdict(list)
        neighbors = defaultdict(list)
        for a, b in connections:
            paths[a].append(b)

            neighbors[a].append(b)
            neighbors[b].append(a)

        #init fringe and visited 
        fringe = []
        for i in neighbors[0]:
            fringe.append(i)

        visited = set()
        visited.add(0) #cities in visited mean they can reach 0

        ans = 0

        #bfs traversal
        while(len(fringe) > 0):
            currCity = fringe.pop()

            if currCity not in visited:
                visited.add(currCity)

                #check if any paths need to be flipped
                canVisit = False
                for i in paths[currCity]:
                    if i in visited:
                        canVisit = True

                if not canVisit:
                    ans += 1

                #update your fringe based on all the neighbors of the city your at
                for i in neighbors[currCity]:
                    if i not in visited:
                        fringe.append(i)
        return ans

