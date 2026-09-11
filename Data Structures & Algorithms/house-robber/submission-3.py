class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        i = 2
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        while i < len(nums):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            i+=1
        return dp[len(nums)-1]
            

