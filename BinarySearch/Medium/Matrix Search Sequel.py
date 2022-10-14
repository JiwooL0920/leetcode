# Given a two-dimensional integer matrix, where every row and column is sorted in ascending order, return whether an integer target exists in the matrix.

# This should be done in \mathcal{O}(n + m)O(n+m) time.

# Constraints

# n, m ≤ 250 where n and m are the number of rows and columns in matrix
# Example 1
# Input
# matrix = [
#     [1, 3, 9],
#     [2, 5, 10],
#     [5, 7, 13]
# ]
# target = 7

class Solution:
    def found(self, row, target):
        lo = 0
        hi = len(row)-1

        while lo <= hi:
            mid = (hi+lo) // 2
            if row[mid] == target:
                return True
            elif target < row[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return False

    def solve(self, matrix, target):
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                if self.found(row, target):
                    return True
        return False
