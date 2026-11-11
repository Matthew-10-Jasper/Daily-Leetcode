
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            profit = price - min_price

            max_profit = max(max_profit, profit)

            min_price = min(min_price, price)

        return max_profit
