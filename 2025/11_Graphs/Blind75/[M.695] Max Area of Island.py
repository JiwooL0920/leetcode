# https://leetcode.com/problems/max-area-of-island/

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

