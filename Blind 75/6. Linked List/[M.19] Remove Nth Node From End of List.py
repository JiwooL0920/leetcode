# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# previous solution
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
        fast = head
        slow = head 
        prev = None 
        
        for i in range(n):
            fast = fast.next
            
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next # we want to delete slow 
        
        if not prev: # target is head 
            head = head.next
        else:
            prev.next = slow.next

        return head
        
# neetcode
# two pointer
# right pointer shifted by n=2, until the nd of the list 
# distance left and right is always 2. then when R = null, L is at n=2 from end of the list 
# but we need to access the node before n. so initialize n at the dummy node (before head)
# Time: O(N)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: 
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left = dummy 
        right = head 
        while n > 0 and right: #n = 0 means we shifted right pointer n times
            right = right.next 
            n -= 1 
        while right: 
            left = left.next 
            right = right.next 
        # delete
        left.next = left.next.next 
        return dummy.next 
        