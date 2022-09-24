# You are given a string s containing "1", "2", "3" and "?". Given that you can replace any “?” with "1", "2" or "3", return the smallest number you can make as a string such that no two adjacent digits are the same.

# Constraints
# n ≤ 100,000 where n is the length of s

# Input
# s = "3?2??"
# Output
# "31212"

# Intuition
# Each "?" can have either a "1" "2" or "3" because the character has at most 2 neighbors.
# Because we want the lexicographically smallest string, we must choose each character greedily to be as small as possible.

# Implementation
# For each s[i] = ?, try to use the smallest character d first - it fails if it matches a neighbor.

# Time Complexity
# \mathcal{O}(n)O(n) - we scan through the string from left to right.

# Space Complexity
# \mathcal{O}(n)O(n) - we use a list to store the answer.

class Solution:
    def solve(self, s):
        A = list(s)
        for i, c in enumerate(A):
            if c == "?":
                for d in "123":
                    A[i] = d
                    if i - 1 >= 0 and A[i] == A[i - 1]:
                        continue
                    if i + 1 < len(A) and A[i] == A[i + 1]:
                        continue
                    break

        return "".join(A)
    
    