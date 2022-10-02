# You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

# Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

# At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

# The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.

 

# Example 1:


# Input: grid = [[2,5,4],[1,5,1]]
# Output: 4
# Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 0 + 4 + 0 = 4 points.
# Example 2:


# Input: grid = [[3,3,1],[8,5,2]]
# Output: 4
# Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 3 + 1 + 0 = 4 points.
# Example 3:


# Input: grid = [[1,3,1,15],[1,3,3,1]]
# Output: 7
# Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.




# first: minimize the number of points collected by second 
# second: maximize number of points
# if play optimally, return points collected by second robot 

# need to understand prefix (and postfix)

""" 
(2) (5)  4                   (0) (0) (4)
 1  (5) (1)                   1  (0) (1)
 
 
pre: 2 7 11
post 7 6 1 
"""

# T: O(N)
# M: O(N)


class Solution:
    def gridGame(self, grid):
        N = len(grid[0])
        preRow1, preRow2 = list(grid[0]), list(grid[1])
        
        for i in range(1, N):
            preRow1[i] += preRow1[i-1]
            preRow2[i] += preRow2[i-1]
            
        res = float("inf") # number of points robot2 can collect 
        
        # first robot chooses which i it will cross  top -> bottom
        for i in range(N):
            top = preRow1[-1] - preRow1[i] # what's remaining in top row for second robot to collect 
            bottom = preRow2[i-1] if i > 0 else 0 
            
            # can either collect top row or bottom 
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)
        
        return res