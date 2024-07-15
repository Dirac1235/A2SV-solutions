class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opSet = {'+', '-', '*', '/'}
        stack = []

        for i in tokens:
            if i not in opSet:
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    stack.append(a + b)
                elif i == '/':
                    stack.append(a / b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '-':
                    stack.append(a - b)
                
        return int(stack[-1])
