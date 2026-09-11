class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 != 0:
            return False
        
        for char in s:
            if char == '[' or char == '{' or char == '(':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                beg = stack.pop()
                comb = beg+char
                if comb == '()' or comb =='[]' or comb == '{}':
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True