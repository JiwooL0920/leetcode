# class Solution:
#     def isBipartite(self, graph):
#         seen = {}
#         for node in range(len(graph)):
#             if node not in seen:
#                 color[node] = 0
#                 stack = [node]
        
#         while stack:
#             n = stack.pop() 
#             for nei in graph[n]:
#                 if nei not in seen:
#                     stack.append(nei)
#                     color[nei] = color[n] ^ 1
                    
                
            