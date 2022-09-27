# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        slow, fast = node, node
        while k and fast.next:
            fast = fast.next
            k -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        return slow.val