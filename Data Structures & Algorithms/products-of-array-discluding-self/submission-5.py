class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,post = [1 for i in range(len(nums))], [1 for i in range(len(nums))]
        curr = 1
        for i in range(len(nums)):
            pre[i] = curr
            curr*= nums[i]
        # [1,1,2,8]
        curr1 = 1
        # [48,24,6,1]
        for i in range(len(nums)-1,-1,-1):
            post[i] = curr1
            curr1*=nums[i]

        res = []
        for i in range(len(nums)):
            res.append(pre[i]*post[i])

        return res
