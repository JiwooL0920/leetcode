# Given a list of integers nums, return whether the number of occurrences of every value in the array is unique.

# Note: Numbers can be negative.

# Input
# nums = [5, 3, 1, 8, 3, 1, 1, 8, 8, 8]
# Output
# True

# T: O(N)
# M: O(N)
from collections import defaultdict 

class Solution:
    def solve(self, nums):
        unique = set()
        occ = defaultdict(int)
        for n in nums:
            occ[n] += 1 
        
        for v in occ.values():
            if v in unique:
                return False 
            unique.add(v)

        return True