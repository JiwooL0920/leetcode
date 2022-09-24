# Given a list of positive integers nums, return the number of integers that have odd number of digits.

# Input
# nums = [1, 800, 2, 10, 3]
# Output
# 4

class Solution:
    def solve(self, nums):
        res = 0
        for n in nums:
            numDigit = 1
            while n // 10:
                n //= 10
                numDigit += 1
            res += 1 if numDigit % 2 != 0 else 0
        return res