class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            beg,end = i+1,len(nums)-1
            diff = -nums[i] 
            while beg < end:

                
                if nums[beg]+nums[end] == diff:
                    res.append([nums[i],nums[beg],nums[end]])
                    beg+=1
                    end-=1
                    while beg < end and nums[end] == nums[end+1]:
                        end-=1
                    while beg < end and nums[beg] == nums[beg-1]:
                        beg+=1
                elif nums[beg]+nums[end] < diff:
                    beg+=1
                else:
                    end-=1
                
        return res