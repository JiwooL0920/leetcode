# Given two lists of integers a and b sorted in ascending order, merge them into one large sorted list.

# Input
# a = [5, 10, 15]
# b = [3, 8, 9]
# Output
# [3, 5, 8, 9, 10, 15]

class Solution:
    def solve(self, a, b):
        res = []
        index_a, index_b = 0, 0 
        while index_a < len(a) and index_b < len(b):
            if a[index_a] < b[index_b]:
                res.append(a[index_a])
                index_a += 1
            else:
                res.append(b[index_b])
                index_b += 1
        res.extend(a[index_a:])
        res.extend(b[index_b:])
        return res