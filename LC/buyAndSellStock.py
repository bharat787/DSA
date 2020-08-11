class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices):
            return 0
        buy = prices[0]
        profit = 0
        for p in prices[1:]:
            if p-buy > profit:
                profit = p-buy
            elif p < buy:
                buy = p
        return profit