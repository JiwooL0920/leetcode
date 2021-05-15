# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

		# O(N) time
		# O(1) space

		head = ListNode()
		curr = head

		while l1 and l2:
			if l1.val <= l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
			curr = curr.next

		if l1:
			curr.next = l1
		elif l2:
			curr.next = l2

		return head.next