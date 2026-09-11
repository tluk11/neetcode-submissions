class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        bcount = 1
        after = [0] * len(nums)
        acount = 1
        for i in range(len(nums)):
            before.append(bcount)
            bcount *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            after[i] = acount
            acount*= nums[i]
        result = []
        for i in range(len(nums)):
            num = before[i]*after[i]
            result.append(num)

        return result

