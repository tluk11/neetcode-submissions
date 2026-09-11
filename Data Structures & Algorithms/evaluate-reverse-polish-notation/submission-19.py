class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok not in {"+", "-", "*", "/"}:
                stack.append(int(tok))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tok == "+":
                    stack.append(num1+num2)
                elif tok == "-":
                    stack.append(num2-num1)
                elif tok == "*":
                    stack.append(num2*num1)
                else:
                    stack.append(int(num2/num1))

        return stack[-1]