# You are given a two-dimensional integer matrix of 1s and 0s, where a 1 represents a bomb and 0 represents an empty cell. When a bomb explodes, all the spaces along on the same row and column are damaged. Return the number of spaces you can stand in to not get damaged.

# Input
# matrix = [
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ]
# Output
# 1

class Solution:
    def solve(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        # safeR = [True for i in range(ROWS)]
        # safeC = [True for i in range(COLS)]
        bombedR, bombedC = set(), set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    print(r,c)
                    bombedR.add(r)
                    bombedC.add(c)
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not (r in bombedR or c in bombedC):
                    res += 1

        return res

