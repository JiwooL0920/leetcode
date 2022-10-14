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


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c):
            if (r in range(ROWS)) and (c in range(COLS)) and ((r,c) not in visit) and (grid[r][c] == "1"):
                visit.add((r,c))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in visit) and (grid[r][c] == "1"):
                    res += 1 
                    dfs(r,c)
        
        return res 