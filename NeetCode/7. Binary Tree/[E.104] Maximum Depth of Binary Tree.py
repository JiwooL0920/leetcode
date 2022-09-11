# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# old solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # O(N) time 
        # O(1) space 
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
# neetcode -- all O(N)
# 1) Recursive DFS
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# 2) Iterative DFS
# preorder DFS -> easiest to do iteratively 
# stack
class Solution:
    def maxDepth(self, root):
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res 
                

# 3) BFS -> not much benefit
# O(N); level order traversal --> count the number of levels 
from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level 