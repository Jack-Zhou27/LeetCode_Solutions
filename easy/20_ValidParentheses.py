class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if(c == '(' or c == '[' or c == '{'):
                stack.append(c)
            else:
                if(len(stack) == 0 or
                    (c == ')' and stack[-1] != '(') or
                    (c == ']' and stack[-1] != '[') or
                    (c == '}' and stack[-1] != '{')
                    ):
                    return False
                stack.pop()
        return len(stack) == 0
