class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for char in nums:
            if char in hashset:
                return True 
            hashset.add(char)
        return False