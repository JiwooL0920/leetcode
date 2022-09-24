# Given a single linked list node, representing a binary number with most significant digits first, return it as an integer.

# Let's consider few examples
# Ex 1:- 1
# Ex 2:- 1 -> 1
# Ex 3:- 1 -> 1 -> 0
# Ex 4:- 1 -> 1 -> 0 -> 1

# Initially we take result ie. res = 0

# In 1st iteration :- res = 0 * 2 + 1 = 1 => res = 1 (Ex 1 )
# In 2nd iteration :- res = 1 * 2 + 1 = 3 => res = 3 (Ex 2)
# In 3rd iteration :- res = 3 * 2 + 0 = 6 => res = 6 (Ex 3)
# In 4th iteration :- res = 6 * 2 + 1 = 13 => res = 13 (Ex 4)

# Time Complexity

# \mathcal{O}(n)O(n). It take O(n) because we traverse through the entire list once.

# Space Complexity
# \mathcal{O}(1)O(1). No matter how big the input list is we only use one variable (only res variable).

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        res = 0
        temp = node
        while temp:
            res = res * 2 + temp.val
            temp = temp.next
        return res