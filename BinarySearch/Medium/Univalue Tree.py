# Given a binary tree root, return whether all values in the tree are the same.

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        val = root.val 
        
        def dfs(root):
            nonlocal val
            if not root:
                return True 
            return root.val == val and dfs(root.left) and dfs(root.right)

        return dfs(root)
        