# Given a binary search tree root and an integer val, determine whether val is in the tree.

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, val):
        if not root:
            return False 
        if root.val == val:
            return True 
        if val < root.val:
            return self.solve(root.left, val)
        else:
            return self.solve(root.right, val)