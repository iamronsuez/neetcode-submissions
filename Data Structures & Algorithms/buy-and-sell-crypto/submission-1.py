class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for ix, val in enumerate(prices):
            if ix != 0:
                for jx, jval in enumerate(prices[:ix]):
                    profit = max(profit, val - jval)
            else:
                profit = 0
        return profit
            