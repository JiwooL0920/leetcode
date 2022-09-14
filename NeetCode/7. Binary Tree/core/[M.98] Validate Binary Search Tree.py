# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# old solution
class Solution(object):
    def isValidBST(self, root):
        if root.left and root.right:
            return root.left.val < root.val and root.val < root.right.val and self.isValidBST(root.left) and self.isValidBST(root.right)
        elif root.left:
            return root.left.val < root.val and self.isValidBST(root.left)
        elif root.right:
            return root.val < root.right.val and self.isValidBST(root.right)
        else:
            return True 
        
# neetcode
# recursive DFS
# have left and right boundary initialized to (-inf, inf)
# left: -inf < 3 < 5  
# right: 5 < 7 < inf 
# Time: O(2N) two comparisons --> O(N)

class Solution:
    def isValidBST(self, root):
        
        # left and right boundaries 
        def valid(node, left, right):
            # empty bst is bst
            if not node: 
                return True
            if not (node.val < right and node.val > left):
                return False 
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
            
        return valid(root, float("-inf"), float("inf"))
    
    