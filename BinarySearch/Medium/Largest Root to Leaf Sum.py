# Given the root to a binary tree root, return the largest sum of any path that goes from the root to a leaf.

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        return root.val + max(self.solve(root.left), self.solve(root.right)) if root else 0