# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        visit = set() 
        islands = 0 
        
        # iterative
        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft() # if you change popleft to q.pop() it will pop the most recent element instead of the first element you added --> iterative DFS 
                directions = [[1,0],[-1,0],[0,1],[0,-1]] #right,left,up,down
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows)) and (c in range(cols)) and grid[r][c] == "1" and ((r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1 
        return islands
    

# 12/9/2024
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0        
        visited = set()

        def bfs(row, col):
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            queue = deque()
            queue.append((row,col))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    r2, c2 = r+dr, c+dc
                    if ( 0 <= r2 < len(grid) 
                        and 0 <= c2 < len(grid[0]) 
                        and grid[r2][c2] == "1" 
                        and (r2, c2) not in visited 
                    ):
                        queue.append((r2, c2))
                        visited.add((r2, c2))
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    num_islands += 1
                    bfs(row, col)

        return num_islands
