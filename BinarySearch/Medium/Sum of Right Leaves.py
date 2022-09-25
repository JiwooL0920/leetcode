# Given a binary tree root, return the sum of all leaves that are right children.

# Input
# root = [0, [4, null, null], [2, [1, [6, null, null], [3, null, null]], [7, null, null]]]
# Output
# 10
from collections import deque 

def solve(root):
    if not root: return 0 
    res = 0 
    q = deque([root])
    
    while q:
        for i in range(len(q)):
            n = q.popleft()
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
                if not n.right.left and not n.right.right:
                    res += n.right.val 
    
    return res 