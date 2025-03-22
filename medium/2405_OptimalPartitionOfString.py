class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        visited = set()
        for c in s:
            if c in visited:
                ans += 1
                visited = set() #clear visited
            visited.add(c)
        return ans + 1
