from collections import deque 

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque([root])
        res = [] 
        
        while q:
            level = []
            for _ in range(len(q)): # iterate just upto the current level
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res