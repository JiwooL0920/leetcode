# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# put into sorted array. traverse in order 
# stack (LIFO)

class Solution:
    def kthSmallest(self, root, k):
        n = 0 
        stack = [] 
        cur = root 
        while cur and stack: 
            # visit every left subtree before visiting cur 
            while cur: 
                stack.append(cur)
                cur = cur.left 
            # when we visited leftmost elem, pop most recently added value from stack
            cur = stack.pop()
            n += 1
            if n == k: 
                return cur.val 
            #now visit all right 
            cur = cur.right 
            
                