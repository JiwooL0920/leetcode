# You are given a two-dimensional list of integers relations. Each element relations[i] contains [a, b] meaning that person a is following person b on Twitter.

# Return the list of people who follow someone that follows them back, sorted in ascending order.

# Constraints
# 0 ≤ n ≤ 100,000 where n is the length of relations

# Input
# relations = [
#     [0, 1],
#     [2, 3],
#     [3, 4],
#     [1, 0]
# ]
# Output
# [0, 1]

class Solution:
    def solve(self, relations):
        seen = set()
        for n1, n2 in relations:
            seen.add((n1,n2))

        print(seen)

        mutual = set()

        for n1, n2 in relations:
            if (n2,n1) in seen:
                mutual.add(n1)
                mutual.add(n2)

        return list(mutual)