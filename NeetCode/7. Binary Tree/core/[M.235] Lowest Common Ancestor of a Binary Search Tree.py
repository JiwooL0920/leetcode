# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# if there's a split, p and q go to different subtree --> common ancestor 
# if p and q are both less than root, check left subtree
# if p and q are both greater than root, check right subtree 
# if one of them is in the left and one of them's in right, we're at ancestor
# if one of them is same as root, that is LCA. 
# Time: O(logn) --> visit one node for every level. so height of tree which is usually log n 
# Memory: O(1)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right 
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left 
            else:
                return cur 

# Sep 5, 2024
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # split occurs
        return root 