# Feb 9, 2025
# https://leetcode.com/problems/valid-sudoku/description/

# Time: O(N^2)
# Space: O(N^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        box = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)

        for i in range(9):
            for j in range(9):
                c = board[i][j]

                # 1) blank
                if c == ".": continue

                # 2) c exists already
                if (
                    c in row[i]
                    or c in col[j]
                    or c in box[(i//3, j//3)]
                ):
                    return False

                # 3) first time seeing c
                row[i].add(c)
                col[j].add(c)
                box[(i//3, j//3)].add(c)

        return True

