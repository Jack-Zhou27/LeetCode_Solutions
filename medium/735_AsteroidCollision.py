class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        if len(asteroids) <= 1:
            return asteroids
        
        stack = []
        for i in asteroids:
            #asteroids only collide if the previous one is moving right, and the current ith asteroid we are analyzing is moving left
            while stack and i < 0 < stack[-1]:
                if abs(i) == stack[-1]:
                    #asteroids destroy one another and we move onto the next ith asteroid
                    stack.pop()
                    break
                elif abs(i) > stack[-1]:
                    #asteroid keeps destroying until it cannot destroy anymore, then we add it to the end of the stack (if it was not annilated and survived)
                    stack.pop()
                    continue
                break
            else:
                stack.append(i)

        return stack
