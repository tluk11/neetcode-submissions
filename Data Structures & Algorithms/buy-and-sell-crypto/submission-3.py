class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        min1,snd = prices[0],prices[1]
        i=1 
        res = 0
        while i<len(prices):
            snd = prices[i]
            
            if min1 < snd:
                res = max(res,snd-min1)
            min1 = min(min1,snd)
            i+=1
            
        return res