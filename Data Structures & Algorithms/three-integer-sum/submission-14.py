class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #nlogn 
        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            need = -nums[i]
            beg = i+1
            end = len(nums)-1
            while beg < end:
                total = nums[beg]+nums[end]
                if total < need:
                    beg+=1
                elif total > need:
                    end-=1
                else:
                    res.append([nums[i],nums[beg],nums[end]])
                    beg+=1
                    end-=1
                    while beg < end and nums[beg] == nums[beg-1]:
                        beg += 1
                    while beg < end and nums[end] == nums[end+1]:
                        end -= 1
        return res

