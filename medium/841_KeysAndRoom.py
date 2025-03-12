class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        fringe = []
        for i in rooms[0]:
            fringe.append(i)

        visited = set()
        visited.add(0)
        
        while len(fringe) > 0:
            currKey = fringe.pop(0)
            if currKey not in visited:
                visited.add(currKey)

                #add keys from the room
                for i in rooms[currKey]:
                    fringe.append(i)
        
        print(visited)
        return len(visited) == len(rooms)
