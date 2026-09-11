class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i in range(len(nums)):
            num = nums[i]
            needed = target-num
            if needed in hashmap:
                return [hashmap[needed],i]
            hashmap[num] = i