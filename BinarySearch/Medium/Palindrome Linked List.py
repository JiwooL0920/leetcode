# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        # find middle
        slow, fast = node, node 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is at the start of right half 
        # reverse right half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # prev is at the head of right half reversed linked list 
        left, right = node, prev 
        while left and right:
            if left.val != right.val:
                return False 
            left = left.next
            right = right.next
        
        return True