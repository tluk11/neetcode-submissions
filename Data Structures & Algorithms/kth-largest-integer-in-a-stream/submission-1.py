import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = []
        for num in nums:
            heapq.heappush(self.queue, num)
            if len(self.queue) > k:
                heapq.heappop(self.queue)  # keep only k largest numbers

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        if len(self.queue) > self.k:
            heapq.heappop(self.queue)  # drop smallest if too many
        return self.queue[0]  # kth largest

