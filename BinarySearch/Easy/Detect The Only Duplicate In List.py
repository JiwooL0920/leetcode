# You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle, there must be a duplicate. Find and return it. There is guaranteed to be exactly one duplicate.

# Bonus: Can you do this in \mathcal{O}(n)O(n) time and \mathcal{O}(1)O(1) space?

# Input
# nums = [1, 2, 3, 1]
# Output
# 1

class Solution:
    def solve(self, nums):
        q = sum(nums)
        n = len(nums)
        v = (n - 1) * (n) // 2
        return q - v