class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        nums.sort()
        length = 1
        maxlength = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] + 1 == nums[i+1]:
                length+= 1
            else:
                maxlength = max(maxlength, length)
                length =1
        return max(maxlength, length) 