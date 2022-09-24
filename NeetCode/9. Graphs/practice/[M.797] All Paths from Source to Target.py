# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# recursive DFS
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        end = len(graph)-1
        
        def dfs(node, path, output):
            if node == end:
                output.append(path)     
            for nei in graph[node]:
                dfs(nei, path+[nei], output)
            
        output = []
        dfs(0,[0],output)
        return output
    
# iterative DFS
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        end = len(graph)-1
        
        stack = [[0]] 
        res = []
        
        while stack:
            path = stack.pop()
            n = path[-1]
            for nei in graph[n]:
                newPath = list(path)
                newPath.append(nei)
                if nei == end:
                    res.append(newPath)
                stack.append(newPath)
                
        return res
                    
# BFS
from collections import deque 

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        end = len(graph)-1
        
        q = deque([[0]])
        res = []
        
        while q:
            path = q.popleft()
            n = path[-1]
            for nei in graph[n]:
                newPath = list(path)
                newPath.append(nei)
                if nei == end:
                    res.append(newPath)
                q.append(newPath)
                
        return res                    