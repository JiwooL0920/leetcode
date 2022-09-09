# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# first value in preorder traversal is always the root 
# then remove root, sublist --> recursion 
# which ones going left/right? -> use in order traversal 
# every value left of root value is going to left subtree, every value right of root value is going to the right subtree 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None 
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])  #preorder from index to mid, inorder beginning up till mid but not including mid 
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root 