# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.


# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2


# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

from collections import defaultdict 

# recursive DFS
class Solution:
    def validPath(self, n, edges, start, end):
        adjList = defaultdict(list)
        
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        visited = set() 
        
        def dfs(node):
            if node == end:
                return True 
            if node not in visited:
                visited.add(node)
                for neighbour in adjList[node]:
                    result = dfs(neighbour)
                    if result:
                        return True 
        
        return dfs(start)
    
    
# iterative DFS
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adjList = defaultdict(list)
        
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()
        
        stack = [source]
        while stack:
            n = stack.pop()
            if n == destination:
                return True 
            if n not in visited:
                visited.add(n)
                for neighbour in adjList[n]:
                    stack.append(neighbour)
        
        return False
        
# bfs with queue
from collections import deque 

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adjList = defaultdict(list)
        
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()
        
        q = deque([source])
        while q:
            for i in range(len(q)):
                n = q.popleft()
                if n == destination:
                    return True 
                if n not in visited:
                    visited.add(n)
                    for neighbour in adjList[n]:
                        q.append(neighbour)
                        
        return False
        