# Given the head of a singly linked list head, return whether the values of the nodes are sorted in a strictly increasing order.

# Input
# head = [1, 5, 9, 9]

# Output
# False

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        curr = head 
        prev = float("-inf")
        while head:
            if prev < head.val:
                prev = head.val
                head = head.next
            else:
                return False
        return True
