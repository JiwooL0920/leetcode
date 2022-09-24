# Undirected. n nodes (1-n). Star -> one center node and exactly n-1 edges. Return center 

# class Solution(object):
#     def findCenter(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: int
#         """
#         # form adjacency dict:
#         adj = defaultdict(list)
#         for n1, n2 in edges:
#             adj[n1].append(n2)
#             adj[n2].append(n1)
        
#         visited = set() 
        
#         for n in adj:
#             if len(adj[n]) > 1:
#                 return n
            
class Solution:
    def findCenter(self, edges):
        
        """ From the Constraints: A valid STAR GRAPH is confirmed. 
		That means the center will be common to every edges. 
		Therefore we can get the center by comparing only first 2 elements"""
 
        # Check if first element of first edge mathches with any element of second edges

        if edges[0][0] == edges [1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]

        #Otherwise second element of first edge will be the answer
        return edges[0][1]                    