# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Previous Solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
            
        
        '''
        1 -> 2 -> 3 -> 4 -> 5
        ^
            nextNode = curr.next = 2
            curr.next = prev = None 
            prev = curr = 1 
            curr = nextNode = 2 
            
        (<-) 1 -> 2 -> 3 -> 4 -> 5
                  ^
            nextNode = curr.next 3
            curr.next = prev = 1 
            prev = curr = 2 
            curr = nextNode = 3 
            
        1 <- 2 -> 3 -> 4 -> 5
                  ^
            nextNode = curr.next = 4
            curr.next = prev = 2 
            prev = curr = 3 
            curr = nextNode = 4
        
        1 <- 2 <- 3 -> 4 -> 5
                       ^
            nextNode = curr.next = 5
            curr.next = prev = 3
            prev = curr = 4
            curr = nextNode = 5
            
        1 <- 2 <- 3 <- 4 -> 5
                            ^
            nextNode = curr.next = None 
            curr.next = prev = 4
            prev = curr = 5
            curr = nextNode = None 
            
        1 <- 2 <- 3 <- 4 <- 5
                               ^
            curr = None
            break while loop 
            
        return prev --> node 5 
            
        
        '''
        
            
# Neetcode
# 1) Two pointers
# Time: O(N)
# Memory: O(1)
class Solution:
    def reverseList(self, head):
        prev, curr = None, head 
        while curr:
            nxt = curr.next # temporary
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