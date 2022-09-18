# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

class Solution:
    def maxAreaOfIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() 
        
        def dfs(r, c):
            # didn't find island
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            visit.add((r,c))
            
            # calculate area 
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        
        maxArea = 0 
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r,c))
                
        return maxArea 
    
    
    
    
# BFS solution
from collections import deque 

class Solution:
    def maxAreaOfIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            area = 1
            
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS)) and (c in range(COLS)) and (grid[r][c] == 1) and ((r,c) not in visited):
                        area += 1
                        q.append((r,c))
                        visited.add((r,c))
            
            return area
        
        maxArea = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))
                
        return maxArea