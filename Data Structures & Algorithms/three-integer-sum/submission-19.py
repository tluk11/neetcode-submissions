class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        left = 0
        while left < len(nums)-2:
            target = -nums[left]

            mid,right = left+1,len(nums)-1
            while mid<right:
                if nums[mid]+nums[right] == target:
                    res.append([nums[left],nums[mid],nums[right]])
                    mid+=1
                    right-=1
                    while mid< right and nums[mid] == nums[mid-1]:
                        mid+=1
                    while mid < right and nums[right] == nums[right+1]:
                        right-=1

                elif nums[mid]+ nums[right] < target:
                    mid+=1
                else:
                    right-=1

            left+=1
            while left < len(nums)-2 and nums[left] == nums[left-1]:
                left+=1

        return res