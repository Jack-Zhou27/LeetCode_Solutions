class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        stack = []
        for p, s in sorted(pairs, reverse = True):
            time = (target - p)/s
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
