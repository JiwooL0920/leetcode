# Given a binary tree root, invert it so that its left subtree and right subtree are swapped and the children are recursively inverted.

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def invert(root):
            if root:
                root.left, root.right = root.right, root.left
                invert(root.left)
                invert(root.right)
        
        invert(root)
        return root