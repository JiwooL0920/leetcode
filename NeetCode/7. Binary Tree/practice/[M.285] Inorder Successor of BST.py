# successor = smallest key greater than p.val 
# T: O(N)
# M: O(1 )
class Solution:
    def inOrderSuccessor(self, root, p):
        successor =  None 
        while root:
            if p.val >= root.val:
                root = root.right 
            else: 
                successor = root 
                root = root.left 
        return successor 
     