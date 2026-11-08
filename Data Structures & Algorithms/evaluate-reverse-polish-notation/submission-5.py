from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for tok in tokens:
            match tok:
                case "+":
                    a,b = stack.pop(),stack.pop()
                    stack.append(a+b)
                case "-":
                    a,b = stack.pop(),stack.pop()
                    stack.append(b-a)
                case "*":
                    a,b = stack.pop(),stack.pop()
                    stack.append(a*b)
                case "/":
                    a,b = stack.pop(),stack.pop()
                    stack.append(int(b/a))
                case _:
                    stack.append(int(tok))
        print(stack)
        return stack.pop()

