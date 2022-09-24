# You are given a singly linked list node containing positive integers. Return the same linked list where every node's next points to the node val nodes ahead. If there's no such node, next should point to null.

# Input
# node = [2, 1, 4, 1]
# Output
# [2, 4]

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        curr = jump = node
        while curr:
            steps = curr.val
            while jump.next and steps:
                jump = jump.next
                steps -= 1
            if steps:
                curr.next = None
                break
            curr.next = jump
            curr = jump
        return node