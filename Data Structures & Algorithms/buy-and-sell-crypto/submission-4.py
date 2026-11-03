class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for ix, val in enumerate(prices):
            min_price = min(min_price, val)
            profit = max(profit, val - min_price)
        return profit
            