from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count task frequencies
        freq = Counter(tasks)
        
        # Step 2: Build max-heap (use negative counts)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)
        
        # Step 3: Queue to track tasks in cooldown
        cooldown = deque()  # stores (task_count, ready_time)
        time = 0
        
        # Step 4: Process tasks
        while max_heap or cooldown:
            time += 1
            
            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1  # decrement count (negative number)
                if cnt != 0:
                    cooldown.append((cnt, time + n))  # add to cooldown
            
            # Move tasks from cooldown back to heap if ready
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])
        
        # Step 5: Return total time
        return time
