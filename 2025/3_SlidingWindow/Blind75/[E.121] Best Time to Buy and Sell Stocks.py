# Jan 31, 2025
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Time: O(N)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy
        r = 1 # sell
        maxP = 0

        while r < len(prices):
            # is it profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # shift all the way right (we want left pointer to be at the minimum)
                l = r
            r += 1

        return maxP


# -------------------------------------------------------------------------------
# Review: Feb 15, 2024
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Time: O(N)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        result = 0
        
        while j < len(prices):
            pi, pj = prices[i], prices[j]
            
            if pi < pj:
                profit = pj - pi
                result = max(result, profit)
            else:
                i = j
            
            j += 1

        return result 