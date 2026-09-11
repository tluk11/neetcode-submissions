class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num]+=1
        heap = []
        for key in hashmap.keys():
            heapq.heappush(heap,(hashmap[key],key))

        while len(heap) > k:
            heapq.heappop(heap)

        return [y for x,y in heap]