# Given the root of a binary tree, invert the tree, and return its root.

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# previous solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 
        
# Neetcode
# everytime we visit node, look at look node, take children and swap position. then recursively run same function on left child and right child
# DFS -> recursive 
class Solution:
    def invertTree(self, root):
        if not root:
            return None 
        # swap the children 
        tmp = root.left 
        root.left = root.right 
        root.right = tmp 
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 
    
    
    
# my own solution
# try 1    
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
        