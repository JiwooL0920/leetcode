# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Recursive DFS
# need to check if left subtrees are equal and right subtrees are equal
# Time: O(p + q)
class Solution:
    def isSameTree(self, p, q):
        # empty trees are equal
        if not p and not q:
            return True 
        # if one tree is empty / if their val is not the same 
        if (not p or not q) or (p.val != q.val):
            return False 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

# 8/11/24
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (not p and not q) or \
                (p and q and p.val == q.val) and \
                self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)
        