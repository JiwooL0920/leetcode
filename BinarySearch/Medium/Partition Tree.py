# Given the root to a binary tree root, return a list of two numbers where the first number is the number of leaves in the tree and the second number is the number of internal (non-leaf) nodes.

# Input
# root = [1, [5, null, null], [3, null, null]]
# Output
# [2, 1]

# 1) BFS
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def solve(self, root):
        res = [0,0]
        q = deque([root])
        
        while q:
            n = q.popleft()
            if n:
                if not n.left and not n.right:
                    res[0] += 1 
                else:
                    res[1] += 1
                q.append(n.left)
                q.append(n.right)
        
        return res


# 2) DFS
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        res = [0,0]

        def dfs(node):
            nonlocal res 
            if node:
                if not node.left and not node.right:
                    res[0] += 1
                else:
                    res[1] += 1 
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return res