# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph. Return the number of connected components in the graph 

# Input: n=5, edges = [[0,1],[1,2],[3,4]]
# output: 2 

# Union Find 
# Time: O(E+V)
# parent array (root parent) 
# rank array (connected components)

# Leet 547
class Solution:
    def countComponents(self, n, edges):
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            res = n1 
            # node itself is its parent; cant go any higher
            while res != par[res]:
                par[res] = par[par[res]] #has grandparent?
                res = par[res]
            return res 
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2) 
            if p1 == p2: 
                return 0  # didn't perform union 
            
            if rank[p2] > rank[p1]:
                par[p1] = p2 
                rank[p2] += rank[p1]
            else: 
                par[p2] = p1 
                rank[p1] += rank[p2]
            return 1 # did perform successful union 
        
        res = n
        for n1, n2 in edges: 
            res -= union(n1, n2) 
            
        return res 
            