# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on day i.

# You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction.
# If no profit is possible, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')

        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return int(max_profit)

sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))