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
        #preorder from index to mid, inorder beginning up till mid but not including mid 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])  
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root 
    

# Time Complexity Analysis:
# Finding the Root Index: The inorder.index(preorder[0]) operation takes (O(n)) time.
# Subarray Creation: Creating subarrays preorder[1:mid+1], inorder[:mid], preorder[mid+1:], and inorder[mid+1:] takes (O(n)) time for each recursive call.
# Recursive Calls: The function makes two recursive calls for the left and right subtrees.
    
# Overall Time Complexity:
# Worst Case: The worst-case time complexity is (O(n^2)).
# Explanation: In each recursive call, finding the root index and creating subarrays takes (O(n)) time. Since there are (n) nodes, the total time complexity is (O(n) + O(n-1) + O(n-2) + ... + O(1) = O(n^2)).