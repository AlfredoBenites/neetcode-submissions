class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0

        for i in range(len(prices)-1):
            if prices[sell] - prices[buy] > 0 and prices[sell] - prices[buy] > profit:
                profit = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1

        return profit
            