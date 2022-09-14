# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# starting from root, does it match the subroot tree
# then check left and right child 
# use helper funciton to compare same tree, check if they are equal 
# null subtree is a subtree of a non-empty tree 

# Time: O(s * t)

class Solution:
    # s = maintree, t = subtree
    def isSubtree(self, s, t):
        # order of conditions is important 
        if not t: return True 
        if not s: return False 
        if self.sameTree(s,t):
            return True 
        # compare t to left subtree of s, and right subtree of s
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def sameTree(self, s, t):
        # both emtpy
        if not s and not t:
            return True 
        # both not empty, compare val of root and recursively check left and right children 
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        # if one if empty and other is nonempty
        return False 
    
    


# my own solution
# try 1
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot:
            return True 
        if not root:
            return False
        if self.isSameTree(root, subRoot): 
            return True 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p, q):
        if not p and not q:
            return True 
        if (not p or not q) or (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        