# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.

# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.




# can't have loops
# every nodes has to be connected 

# input value for nodes = visited --> graph is connected 
# have a prev variable to keep track of previously visited nodes 

# recursive DFS, adj list 
# Time and Mem O(E+V)

def validTree(self, n, edges):
    # empty graph is tree
    if not n:
        return True 
    # create adj list 
    adj = { i:[] for i in range(n) }
    for n1, n2 in edges: 
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    visit = set() 
    # i = value of node we're visited
    def dfs(i, prev): 
        # detected a loop
        if i in visit:
            return False 
        visit.add(i) 
        for j in adj[i]:
            # j = adj node of i
            if j == prev: 
                continue 
            if not dfs(j, i):
                return False #detected a loop  
        return True 
    
    return dfs(0, -1) and n == len(visit) # default start prev dummy value -1 
        
