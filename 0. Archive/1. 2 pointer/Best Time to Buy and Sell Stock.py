'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
'''

from typing import List

class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     buy_price = prices[0]
    #     profit = 0

    #     for p in prices[1:]:
    #         if buy_price > p:
    #             buy_price = p
            
    #         profit = max(profit, p - buy_price)
        
    #     return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1
        
        return max_profit
            
            


solution = Solution()

prices = [
    [7,1,5,3,6,4],
    [7,6,4,3,1],
    [2,4,1]
]

for price in prices:
    print(solution.maxProfit(price))