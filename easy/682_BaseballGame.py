class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == "C":
                stack.pop()
            elif c == "D":
                stack.append(stack[-1] * 2)
            elif c == "+":
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(c))
        return sum(stack)
