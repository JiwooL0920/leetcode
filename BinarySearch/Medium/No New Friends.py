# You are given n people represented as an integer from 0 to n - 1, and a list of friends tuples, where person friends[i][0] and person friends[i][1] are friends.

# Return whether everyone has at least one friend.

# Input
# n = 3
# friends = [
#     [0, 1],
#     [1, 2]
# ]
# Output
# True
from collections import defaultdict 

class Solution:
    def solve(self, n, friends):
        adjList = defaultdict(list)
        for n1, n2 in friends:
            adjList[n1] = n2
            adjList[n2] = n1 
        
        return len(adjList) == n
        