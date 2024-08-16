# https://leetcode.com/problems/symmetric-tree/description/

# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Input: root = [1,2,2,null,3,null,3]
# Output: false

# time: O(h) worst case, O(log h) best case if tree is completely balanced
 

class Solution:
    def isMirror(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        else:
            return left.val == right.val and \
                    self.isMirror(left.left,right.right) and \
                    self.isMirror(left.right, right.left) 
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
        