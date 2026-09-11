class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}
        index = 0 
        for num in nums:
            otherNum = target - num
            if otherNum in myHash:
                return [myHash[otherNum],index]
            myHash[num] = index
            index+=1