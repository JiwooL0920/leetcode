# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

class Solution:
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # run binary search on column
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bot = row - 1
            # target is in range of the row 
            else: 
                break 
        
        # none of the rows contain target 
        if not (top <= bot): 
            return False 
         
        # run binary search on rows 
        row = (top+bot) // 2 
        l, r = 0, COLS - 1
        while l <= r: 
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1 
            elif target < matrix[row][m]:
                r = m - 1 
            else: 
                return True 
            
        # never found target value
        return False 