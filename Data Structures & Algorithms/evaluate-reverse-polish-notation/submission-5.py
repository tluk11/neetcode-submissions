class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok != '+' and tok!= '-' and tok != '*' and tok != '/':
                stack.append(int(tok))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tok == '+':
                    num3 = num1+ num2 
                elif tok == '*':
                    num3 = num1*num2
                elif tok == '/':
                    num3 = int(num2/num1)
                elif tok == '-':
                    num3 = num2 - num1
                stack.append(num3)
        return stack.pop()