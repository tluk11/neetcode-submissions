class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        numset = set(nums)
        seen = set()
        maxlen = 0
        # try and start at the beginning of longest consecutive sequence
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            temp = num-1
            len = 1
            while temp in numset:
                seen.add(temp)
                len+=1
                temp-=1

            maxlen = max(maxlen,len)
        return maxlen
