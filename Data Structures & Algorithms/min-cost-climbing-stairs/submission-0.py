from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return min(cost[0], cost[1])
        
        # In-place DP: cost[i] = min cost to reach step i
        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        
        # You can reach the top from either of the last two steps
        return min(cost[-1], cost[-2])
