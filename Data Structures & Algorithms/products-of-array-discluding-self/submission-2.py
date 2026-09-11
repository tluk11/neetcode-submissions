class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 1
        pre = 1
        res = [1]*(len(nums))
        for i in range(len(nums)):
            res[i] = pre  
            pre*= nums[i]        
        post = 1
        
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post*= nums[i]
        return res
            
        # [1,2,4,6] -> [48,48,24,6]