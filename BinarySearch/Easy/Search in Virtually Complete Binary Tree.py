# Consider a complete binary tree of n nodes whose values are 1 to n. The root has value of 1, its left child is 2 and its right child is 3. In general, nodes' values are labelled 1 to n in level order traversal.

# You are given a binary tree root and an integer target. Given that the root was originally a complete binary tree whose values were labelled as described above, and that some of the subtrees were deleted, return whether target exists in root.

# Bonus: solve in \mathcal{O}(h)O(h) time where h is the height of the tree.

# Constraints

# 1 ≤ n ≤ 100,000 where n is the number of nodes in root

# Input
# root = [1, [2, [4, null, null], null], [3, [6, null, null], [7, null, null]]]
# target = 6
# Output
# True

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def solve(self, root, target):
        
        q = deque([root])

        while q:
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    if n.val == target:
                        return True
                    q.append(n.left)
                    q.append(n.right)
        
        return False