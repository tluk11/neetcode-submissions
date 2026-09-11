class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        mylist = []
        def dfs(open1,close,s):
            if open1 + close == n*2:
                mylist.append(s)
                return
            if open1 < n:
                dfs(open1 +1,close, s+"(")
            if open1 > close:
                 dfs(open1,close+1, s+")")
        dfs(0,0,"")
        return mylist            

