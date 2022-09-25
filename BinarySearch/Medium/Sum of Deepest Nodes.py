# Given a binary tree root, find the sum of the deepest node values.

# Input
# root = [0, [5, null, null], [9, [1, [4, null, null], [2, null, null]], [3, null, null]]]
# Output
# 6

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def solve(self, root):
        res = 0 
        q = deque([root])

        while q:
            hasLevel = False
            levelSum = 0
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    hasLevel = True 
                    levelSum += n.val 
                    q.append(n.left)
                    q.append(n.right)
            if hasLevel:
                res = levelSum
        
        return res

