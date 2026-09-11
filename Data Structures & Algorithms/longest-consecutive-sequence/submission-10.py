class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        res = 1
        for num in nums:
            if (num-1) not in nums:
                length = 1
                while (num+1) in nums:
                    num+=1
                    length+=1
                res = max(res,length)
        return res
                