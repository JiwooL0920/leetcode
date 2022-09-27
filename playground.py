from collections import deque 

class Solution:
    def solve(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])

        # differentiate island 
        def separateIsland():
            def dfs(r, c):
                if (r in range(ROWS)) and (c in range(COLS)) and (matrix[r][c] == 1):
                    matrix[r][c] = 2
                    dfs(r+1, c)
                    dfs(r-1, c)
                    dfs(r, c+1)
                    dfs(r, c-1)

            for r in range(ROWS):
                for c in range(COLS):
                    if matrix[r][c] == 1:
                        dfs(r,c)
                        return 

        separateIsland()
        print(matrix)

    
        # start from island 2, find island 1
        def findBridge(r,c):
            visit = set((r,c))
            q = deque([(r,c)])
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            res = 0
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    if (rr in range(ROWS)) and (cc in range(COLS)) and ((rr,cc) not in visit):
                        if matrix[rr][cc] == "1":
                            return res
                        if (matrix[rr][cc] == 0):
                            res += 1
                            visit.add((rr,cc))
                            q.append((rr,cc))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 2:
                    return findBridge(r,c) -1
