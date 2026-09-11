class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol,res = [],[]
        def backtrack(i):
            if i >= len(s):
                res.append(sol[:])
                return 
            for j in range(i,len(s)):
                if isP(i,j):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()
        
        def isP(beg,end):
            while beg<end:
                if s[beg] == s[end]:
                    beg+=1
                    end-=1
                else:
                    return False
            return True
        backtrack(0)
        return res