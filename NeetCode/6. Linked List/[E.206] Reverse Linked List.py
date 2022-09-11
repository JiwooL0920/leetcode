# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Previous Solution
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
            
# Neetcode
# 1) Two pointers
# Time: O(N)
# Memory: O(1)
class Solution:
    def reverseList(self, head):
        prev, curr = None, head 
        while curr:
            nxt = curr # temporary
            curr.next = prev
            prev = curr 
            curr = nxt 
        return prev 

# 2) Recursive 
# Time: O(N)
# Memory: O(N)
class Solution:
    def reverseList(self, head):
        if not head:
            return None 
        newHead = head 
        if head.next: 
            newHead = self.reverseList(head.next)
            head.next.next = head #reverse link between next node and head 
        head.next = None #if head happens to be first element in list 
        return newHead 