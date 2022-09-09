# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

#previous solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False
        
'''
3 -> 2 -> 0 -> -4
     ^          |
     |__________|
     
slow = 3
fast = 2 

while loop
    fast: 2, fast.next = 0
    slow != fast 
    slow = 2
    fast = -4 
    
    fast: -4. fast.next = 2
    slow != fast
    slow = 0
    fast = 0 
    
    fast: 0, fast.next = -4
    slow = fast = 0 
    return True 
'''

# Needcode
# Hashset 
# Time: O(N)
# Mem: O(N)
# Two pointer -- Floyd's Tortoise & Hare 
# Mem: O(1)
class Solution:
    def hasCycle(self, head):
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                return True 
        return False 