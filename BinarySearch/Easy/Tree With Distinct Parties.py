# Given a binary tree root, return the number of perfect nodes. A perfect node has two properties:

# Has both children
# The sum of one subtree is even and the sum of the other subtree is odd
    
# Input
# root = [1, [5, null, null], [3, [4, null, null], [7, null, null]]]
# Output
# 2


class Solution:
    def solve(self, root):
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if root.left and root.right:
                ans += ((l % 2) + (r % 2)) % 2
            return root.val + l + r

        dfs(root)
        return ans