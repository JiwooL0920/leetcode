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