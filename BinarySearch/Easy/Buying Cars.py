# Given a list of integers prices representing prices of cars for sale, and a budget k, return the maximum number of cars you can buy.

# T: O(N)
# M: O(1)

class Solution:
    def solve(self, prices, k):
        prices.sort()
        res = 0
        for p in prices:
            if k and p <= k:
                res += 1
                k -= p
        return res