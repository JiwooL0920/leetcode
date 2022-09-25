# Given a binary tree root, return the number of nodes that are an only child. A node x is an only child if its parent has exactly one child (x).

# Input
# root = [0, [4, null, null], [2, [1, [3, null, null], null], null]]
# Output
# 2

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        res = 0

        def dfs(node):
            nonlocal res 
            if node:
                if (node.left and not node.right) or (not node.left and node.right):
                    res += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return res
        