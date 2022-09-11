# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# buy low, sell high 
class Solution:
    def maxProfit(self, prices):
        l, r = 0, 1 #left=buy, right=sell
        maxP = 0 
        while r < len(prices):
            # profitable ? 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r # left point at minimum  
            r += 1 # regardless of condition, update right pointer
        return maxP 