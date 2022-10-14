# Given a two-dimensional integer matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

# Note: Neighbors can only be directly horizontal or vertical, not diagonal.

# Constraints

# n, m ≤ 100 where n and m are the number of rows and columns in matrix.
# Example 1
# Input
# matrix = [
#     [1, 1],
#     [1, 0]
# ]
# Output
# 1
# Example 2
# Input
# matrix = [
#     [1, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0],
#     [0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 1],
#     [1, 1, 0, 0, 1]
# ]
# Output
# 4
# Example 3
# Input
# matrix = [
#     [0, 1],
#     [1, 0]
# ]
# Output
# 2

class Solution:
    def solve(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])

        visit = set() 

        def dfs(r,c):
            if (r in range(ROWS)) and (c in range(COLS)) and ((r,c) not in visit) and (matrix[r][c] == 1):
                visit.add((r,c))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in visit) and (matrix[r][c] == 1):
                    res += 1
                    dfs(r,c)
        return res         