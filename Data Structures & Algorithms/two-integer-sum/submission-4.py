class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            num = nums[i]
            remainder = target-num
            if remainder in hashmap:
                return [hashmap[remainder],i]
            hashmap[nums[i]]=i
        return