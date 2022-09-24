# Given a two-dimensional integer list intervals of the form [start, end] representing intervals (inclusive), return their intersection, that is, the interval that lies within all of the given intervals.

# You can assume that the intersection will be non-empty.

# Input
# intervals = [
#     [1, 100],
#     [10, 50],
#     [15, 65]
# ]
# Output
# [15, 50]

class Solution:
    def solve(self, intervals):
        lower = float("-inf")
        upper = float("inf")
        
        for start, end in intervals:
            lower = max(lower, start)
            upper = min(upper, end)
        
        return [lower, upper]