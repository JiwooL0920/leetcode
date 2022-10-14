# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


# T:O(N)
# M: O(N)
# recursive
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        
        def dfs(node):
            if not node: return 
            
            res.append(node.val)
            for c in node.children:
                dfs(c)
        
        dfs(root)
        return res
    
# same complexities
# recursive
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if not node: continue
            res.append(node.val)
            for c in node.children[::-1]:
                stack.append(c)
        
        return res
            