class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        candidates.sort()
        def backtrack(i,total):
            if total == target:
                res.append(sol[:])
                return
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break
                sol.append(candidates[j])
                backtrack(j+1,total+candidates[j])
                sol.pop()
            

        backtrack(0,0)

        return res