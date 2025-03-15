class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if(i not in "+-*/"):
                stack.append(int(i))
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                
                if(i == "+"):
                    stack.append(temp1 + temp2)
                elif(i == "-"):
                    stack.append(temp2 - temp1)
                elif(i == "*"):
                    stack.append(temp1 * temp2)
                else:
                    stack.append(int(temp2 / temp1))
                
        return stack[0]
