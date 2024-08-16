# https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 6

# Example 2:
# Input: root = []
# Output: 0

# Example 3:
# Input: root = [1]
# Output: 1
 
# Constraints:
# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return 0
    
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left, right = root, root
        hl, hr = 0 , 0
        while left:
            hl += 1
            left = left.left
        while right:
            hr += 1
            right = right.right
        
        # all levels are full
        if hl == hr:
            return (2 ** hl) - 1
        
        # last level is not full
        return 1 + \
                self.countNodes(root.left) + \
                self.countNodes(root.right)