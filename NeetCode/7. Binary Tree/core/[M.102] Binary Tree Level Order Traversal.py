# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]


# old solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution():
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root] 
        res = []
        
        while queue:
            currLevel = []
            nextLevel = []
            for node in queue:
                currLevel.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(currLevel)
            queue = nextLevel 

        return res
                    

# neet code 
# BFS, queue 
# insert element to the right, pop from left (FIFO)
# for each level, add elems in queue. form the level list
# as we pop values, insert its children to queue 
# start with [root] and repeat until queue is empty 
# Time: O(N)
# Mem: O(N/2) --> biggest level of tree in bst --> O(N)

from collections import deque

class Solution():
    def levelOrder(self, root):
        res = []
        q = deque() 
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft() 
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
            
        return res 
        
    