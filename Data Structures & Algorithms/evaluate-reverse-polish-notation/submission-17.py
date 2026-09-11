class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        hashs = set()
        hashs.add("+")
        hashs.add("-")
        hashs.add("*")
        hashs.add("/")
        for tok in tokens:
            
            if tok in hashs:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                temp = 0
                if tok == "+":
                    temp = num1+num2
                elif tok == "-":
                    temp = num2-num1
                elif tok == "*":
                    temp = num2*num1
                elif tok == "/":
                    temp = int(num2/num1)
                stack.append(temp)
            else:
                stack.append(tok)
            
        return int(stack[-1])