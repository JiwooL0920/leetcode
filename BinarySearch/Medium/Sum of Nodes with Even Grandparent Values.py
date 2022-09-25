# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 


class Solution:
    def solve(self, root):
        s = 0
        if not root:
            return
        q = deque([(None, None, root)])
        while q:
            gp, p, c = q.popleft()
            if gp and gp.val % 2 == 0:
                s += c.val
            if c.left:
                q.append((p, c, c.left))
            if c.right:
                q.append((p, c, c.right))
        return s


class Solution:
    def solve(self, root, parent_is_even=False, grandparent_is_even=False):
        if not root:
            return 0
        else:
            result = 0

            if grandparent_is_even:
                result += root.val

            root_is_even = root.val % 2 == 0
            result += self.solve(root.left, root_is_even, parent_is_even)
            result += self.solve(root.right, root_is_even, parent_is_even)
            return result
