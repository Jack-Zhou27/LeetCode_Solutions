class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def isValid(currState, maze):
            x = currState[0]
            y = currState[1]
            if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == ".":
                return True
            return False
            
        def isGoalState(currState, visited):
            x = currState[0]
            y = currState[1]
            if (x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[0]) - 1) and (x,y) not in visited:
                return True
            return False


        fringe = []
        fringe.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((fringe[0][0], fringe[0][1]))

        while len(fringe) > 0:
            currPos = fringe.pop(0)
            nextX = currPos[0]
            nextY = currPos[1]
            currDist = currPos[2]

            #north
            nextState = (nextX, nextY + 1, currDist + 1)
            if (nextX, nextY + 1) not in visited and isValid(nextState, maze):
            
                if isGoalState(nextState, visited):
                    return nextState[2]
                
                visited.add((nextX, nextY + 1))
                
                fringe.append(nextState)

            #east
            nextState = (nextX + 1, nextY, currDist + 1)
            if (nextX + 1, nextY) not in visited and isValid(nextState, maze):

                if isGoalState(nextState, visited):
                    return nextState[2]

                visited.add((nextX + 1, nextY))
                
                fringe.append(nextState)
                
            #south
            nextState = (nextX, nextY - 1, currDist + 1)
            if (nextX, nextY - 1) not in visited and isValid(nextState, maze):

                if isGoalState(nextState, visited):
                    return nextState[2]

                visited.add((nextX, nextY - 1))
                
                fringe.append(nextState)

            #west
            nextState = (nextX - 1, nextY, currDist + 1)
            if (nextX - 1, nextY) not in visited and isValid(nextState, maze):

                if isGoalState(nextState, visited):
                    return nextState[2]
                
                visited.add((nextX - 1, nextY))

                fringe.append(nextState)
        
        return -1
