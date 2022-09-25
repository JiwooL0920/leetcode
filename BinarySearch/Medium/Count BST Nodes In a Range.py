# Given a binary search tree root, and integers lo and hi, return the count of all nodes in root whose values are between [lo, hi] (inclusive).

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        count = 0

        def traverse(node):
            nonlocal count
            if node:
                if lo <= node.val <= hi:
                    count += 1
                    traverse(node.left)
                    traverse(node.right)
                elif node.val < lo:
                    traverse(node.right)
                elif hi < node.val:
                    traverse(node.left)

        traverse(root)
        return count
