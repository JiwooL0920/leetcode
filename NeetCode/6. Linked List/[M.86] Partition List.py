# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head, x):
        left, right = ListNode(), ListNode() 
        ltail, rtail = left, right 
        
        while head:
            if head.val < x:
                ltail.ext = head 
                ltail = ltail.next 
            else:
                rtail.next = head 
                rtail = rtail.next 
            
            head = head.next 
            
        ltail.next = right.next
        rtail.next = None 
        return left.next 