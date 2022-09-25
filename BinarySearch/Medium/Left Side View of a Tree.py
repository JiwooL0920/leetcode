# Given a binary tree root, return the leftmost node's value on each level of the tree.

# Input
# root = [0, [5, null, null], [2, null, [1, null, null]]]
# Output
# [0, 5, 1]

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 


class Solution:
    def solve(self, root):
        res = []
        q = deque([root])
        while q:
            firstLevel = True
            for i in range(len(q)):
                n = q.popleft() 
                if n:
                    if firstLevel:
                        res.append(n.val)
                        firstLevel = False
                    q.append(n.left)
                    q.append(n.right)
        return res