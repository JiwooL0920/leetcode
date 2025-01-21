# https://leetcode.com/problems/island-perimeter/

# time/memory: O(n*m)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visit = set()

        def dfs(i, j):
            # check if coordinate is within range and if its not a land
            # we know we have a perimeter if we found water
            if i >= len(grid) or j >= len(grid[0]) \
                or i < 0 or j < 0 \
                or grid[i][j] == 0:
                   return 1

            # rule out land thats been visited already 
            if (i, j) in visit:
                return 0
            
            # mark the new found land as visited
            visit.add((i,j))

            # recursively inspect the 4 edges to this coordinate (dfs)
            perimeter = dfs(i, j+1)
            perimeter += dfs(i+1, j)
            perimeter += dfs(i, j-1)
            perimeter += dfs(i-1, j)

            return perimeter

        # To start dfs, first find a land
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs (i, j)
        

