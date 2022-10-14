# You are given a two-dimensional integer matrix of 1s and 0s. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water. You can assume that the edges of the matrix are surrounded by water.

# Return the area of the largest island in matrix.

# Constraints

# n, m ≤ 250 where n and m are the number of rows and columns in matrix
# Example 1
# Input
# matrix = [
#     [0, 0, 0, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0]
# ]
# Output
# 7
# Explanation
# The largest island in the center has an area of 7 units.

class Solution:
    def solve(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])

        visit = set() 

        def dfs(r,c):
            if (r in range(ROWS)) and (c in range(COLS)) and ((r,c) not in visit) and (matrix[r][c] == 1):
                visit.add((r,c))
                res = 1
                res += dfs(r+1, c)
                res += dfs(r-1, c)
                res += dfs(r, c+1)
                res += dfs(r, c-1)
                return res 
            else:
                return 0 

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in visit) and (matrix[r][c] == 1):
                    res = max(res, dfs(r,c))
        return res 