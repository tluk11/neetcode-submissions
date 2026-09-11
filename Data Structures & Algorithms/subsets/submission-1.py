class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        copy = []
        def backtrack(n):
            if n == len(nums):
                res.append(copy[:])
                return
            backtrack(n+1)
            copy.append(nums[n])
            backtrack(n+1)

            copy.pop()
        backtrack(0)
        return res