# Given an 2D matrix of 0s and 1s, a 1 represents land and 0 represents water. An island is a group of 1's that are surrounded by 0s or by the border. Find all the islands that are completely surrounded by water and modify them into 0s.

# An island is completed surrounded by water if all of the neighbours are water (that is, none of the neighbours are borders).

# Note: Neighbours can only be directly horizontal or vertical, not diagonal.

# Constraints

# n, m ≤ 250 where n and m are the number of rows and columns in matrix

# Input
# board = [
#     [1, 0, 0, 0],
#     [0, 1, 1, 0],
#     [0, 0, 0, 0]
# ]
# Output
# [
#     [1, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]

from collections import deque

class Solution:
    def solve(self, board):
        ROWS, COLS = len(board), len(board[0])

       # capture islands that touch border 1 -> 2
        def bfs(row, col):
            visit = set((row, col))
            q = deque([(row, col)])
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                r, c = q.popleft()
                board[r][c] = 2
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc 
                    if (newR in range(ROWS)) and (newC in range(COLS)) and ((newR, newC) not in visit) and (board[newR][newC] == 1):
                        visit.add((newR, newC))
                        q.append((newR, newC))

        # dfs solution
        def dfs(r, c):
            if (r in range(ROWS)) and (c in range(COLS)) and (board[r][c] == 1):
                board[r][c] = 2
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

                
        for r in range(ROWS):
           for c in range(COLS):
               if (board[r][c] == 1) and (r in [0,ROWS-1] or c in [0,COLS-1]):
                   bfs(r, c)
                   # dfs(r, c)

        # capture islands surrounded by water 1 -> 0
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 1):
                    board[r][c] = 0

        # change 2->1
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 2):
                    board[r][c] = 1 

        return board