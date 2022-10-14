# You are given a binary tree root with each node containing single digits from 0 to 9. Each path from the root to the leaf represents a number with its digits in order.

# Return the sum of numbers represented by all paths in the tree.

# Example 1
# Input
# Visualize
# root = [3, [5, null, null], [2, [1, null, null], [4, null, null]]]
# Output
# 680
# Explanation
# We have the following numbers represented by paths:

# 35 (3 → 5)
# 321 (3 → 2 → 1)
# 324 (3 → 2 → 4)
# Example 2
# Input
# Visualize
# root = [1, [2, null, null], [3, null, null]]
# Output
# 25
# Explanation
# We have 12 + 13 = 25.

class Solution:
    def paths(self, root, sums):
        if not root:
            return 0
        if not root.left and not root.right:
            return sums * 10 + root.val
        else:
            return self.paths(root.left, sums * 10 + root.val) + self.paths(
                root.right, sums * 10 + root.val
            )

    def solve(self, root):
        return self.paths(root, 0)