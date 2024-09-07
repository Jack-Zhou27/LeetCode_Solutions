class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for c in s:
            if c == "]":
                currStr = ""
                
                while stack and stack[-1] != "[":
                    currStr += stack.pop()

                stack.pop()

                count = ""
                while stack and stack[-1] in "0123456789":
                    count += stack.pop()

                for i in range ( int(count[::-1]) ):
                    for j in reversed(currStr):
                        stack.append(j)
            else:
                stack.append(c)
        reversed(stack)
        return "".join(stack)
