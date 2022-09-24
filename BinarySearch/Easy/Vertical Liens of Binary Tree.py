# Given a binary tree root, return the number of unique vertical lines that can be drawn such that every node has a line intersecting it. Each left child is angled at 45 degrees to its left, while the right child is angled at 45 degrees to the right.

# For example, root and root.left.right are on the same vertical line

# Input
# root = [1, [2, [3, null, null], null], [4, null, [5, null, null]]]
# Output
# 5

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        left = right = 0 

        def dfs(root, x):
            nonlocal left, right
            if not root:
                return
            left = min(x, left)
            right = max(x, right)
            dfs(root.left, x-1)
            dfs(root.right, x+1)
        
        dfs(root,0)
        return right - left + 1