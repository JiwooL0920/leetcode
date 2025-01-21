# https://leetcode.com/problems/number-of-islands/

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

