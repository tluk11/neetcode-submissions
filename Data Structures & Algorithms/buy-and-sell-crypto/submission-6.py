class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = prices[0]
        maxProfit = 0
        for price in prices:
            if price > buy:
                maxProfit = max(maxProfit, price-buy)
            if price < buy:
                buy = price

        return maxProfit
