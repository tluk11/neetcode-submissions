class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1
        frequency = [[] for _ in range(len(nums) + 1)]

        for num,counts in count.items():
            frequency[counts].append(num)
        res = []
        for i in range(len(frequency)-1,-1,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        
