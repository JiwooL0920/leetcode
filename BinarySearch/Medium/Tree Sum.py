# Given a binary tree root, return the sum of all values in the tree.

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root:
            return root.val + self.solve(root.right) + self.solve(root.left)
        else:
            return 0