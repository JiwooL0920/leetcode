# 01-09-25

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        DIR = [(1,0), (-1,0), (0,1), (0,-1)]

        max_area = 0
        visited = set()


        def bfs(row, col):
            area = 1
            visited.add((row, col))
            queue = deque([(row, col)])
        
            while queue:
                r, c = queue.popleft()
                for dr, dc in DIR:
                    r2, c2 = r+dr, c+dc
                    if (
                        0 <= r2 < R
                        and 0 <= c2 < C
                        and grid[r2][c2] == 1
                        and (r2, c2) not in visited
                    ):
                        visited.add((r2, c2))
                        queue.append((r2, c2))
                        area += 1
    
            return area


        for r in range(R):
            for c in range(C):
                if (
                    (r,c) not in visited
                    and grid[r][c] == 1
                ):
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area


# Solution without using set for visited
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         DIR = [0, 1, 0, -1, 0]
        
#         def bfs(r, c):
#             q = deque([(r, c)])
#             grid[r][c] = 0
#             ans = 0
#             while q:
#                 r, c = q.popleft()
#                 ans += 1
#                 for i in range(4):
#                     nr, nc = r + DIR[i], c + DIR[i+1]
#                     if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0: continue
#                     grid[nr][nc] = 0  # Mark this square as visited
#                     q.append((nr, nc))
#             return ans
        
#         ans = 0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 1:
#                     ans = max(ans, bfs(r, c))
#         return ans