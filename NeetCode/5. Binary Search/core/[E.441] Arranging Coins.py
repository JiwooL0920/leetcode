# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        needed = 1 
        while True:
            if n < needed:
                return res 
            res += 1
            n -= needed 
            needed += 1
            
# better way = binary search, gauss formula O(logN)            