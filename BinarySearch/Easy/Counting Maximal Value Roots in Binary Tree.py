# Given a binary tree root, count and return the number of nodes where its value is greater than or equal to the values of all of its descendants.

# Input
# root = [6, [3, null, null], [2, [6, null, null], [4, null, null]]]
# Output
# 4

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return 0

        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val >= max(left, right):
                result += 1
            x = max(node.val, left, right)
            return x

        dfs(root)
        return result
