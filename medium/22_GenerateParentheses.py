class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtracking(openCount, closeCount):
            if openCount == closeCount == n:
                ans.append("".join(stack))
                return
            if openCount < n:
                stack.append("(")
                backtracking(openCount + 1, closeCount)
                stack.pop()
            if(closeCount < openCount and closeCount < n):
                stack.append(")")
                backtracking(openCount, closeCount + 1)
                stack.pop()
        
        backtracking(0, 0)
        return ans

            
