class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        yesterday, today = 0 ,1
        maxP = 0

        while today < len(prices):
            if prices[yesterday] < prices[today]:
                profit = prices[today] - prices[yesterday]
                maxP = max(maxP, profit)
            else:
                yesterday = today
            today +=1
        return maxP