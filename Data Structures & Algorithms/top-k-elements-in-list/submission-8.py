class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num]+=1

        l = [[] for i in range(len(nums)+1)]
        for key in hashmap.keys():
            l[hashmap[key]].append(key)

        res = []

        for i in range(len(l)-1,-1,-1):
            nu = l[i]
            for n in nu:
                res.append(n)
                if len(res) == k:
                    return res

        return res