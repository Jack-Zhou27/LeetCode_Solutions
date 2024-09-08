class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [0] * (len(cost) + 1)
        cache[len(cost)] = 0
        cache[len(cost) - 1] = cost[len(cost) - 1]
        for i in range(len(cost) - 1, -1, -1):
            cache[i - 1] = cost[i - 1] + min(cache[i], cache[i + 1])
        return min(cache[0], cache[1])
