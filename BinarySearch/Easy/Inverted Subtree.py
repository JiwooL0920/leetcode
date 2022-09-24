# from contextlib import nullcontext


# A tree is inversion of another if:
#     - both trees are null 
#     - left and right children are optionally swapped 
# source = smaller tree

# T: O(N*M)
# M: O(N)

class solution:
    def solve(self, s, t):
        if not t:
            return s == t 
        return self.isInv(s,t) or self.solve(s, t.left) or self.solve(s, t.right)
    
    def isInv(self, t1, t2):
        if not t1 or not t2:
            return t1 == t2 
        if t1.val != t2.val:
            return False 
        return (self.isInv(t1.left, t2.right) and self.isInv(t1.right, t2.left)) or (self.isInv(t1.left, t2.left) and self.isInv(t1.right, t2.right))