# Given a binary tree root where each node contains a digit from 0-9, return whether its in-order traversal is a palindrome.

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        res = []
        
        def inOrder(node):
            if node:
                inOrder(node.left)
                res.append(node.val)
                inOrder(node.right)

        inOrder(root)

        l, r = 0, len(res)-1
        while l <= r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        
        return True