class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]

        nums.sort()

        def backtrack(i,total):
            if total == target:
                res.append(sol[:])
                return

            if i == len(nums) or total > target:
                return 

            sol.append(nums[i])
            backtrack(i,total+nums[i])
            sol.pop()
            backtrack(i+1,total)

        backtrack(0,0)

        return res
