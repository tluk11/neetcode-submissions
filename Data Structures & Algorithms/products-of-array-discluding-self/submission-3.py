class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*(len(nums)+1)
        post = [1]*(len(nums)+2)
        for i in range(len(nums)): # fill out pre array 
            pre[i+1] = pre[i]*nums[i]

        # fill out post array 
        for i in range(len(nums)-1,-1,-1):
            post[i] = post[i+1]*nums[i]
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = pre[i]*post[i+1]

        return res
