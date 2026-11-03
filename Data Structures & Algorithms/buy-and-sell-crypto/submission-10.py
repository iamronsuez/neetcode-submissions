class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day, sell_day = 0 ,1
        maxP = 0

        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                maxP = max(maxP, profit)
            else:
                buy_day = sell_day
            sell_day +=1
        return maxP