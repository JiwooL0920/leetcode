graph = {
	1: [2, 3, 8],
	2: [1, 7],
	3: [1, 4, 5],
	4: [3, 5],
	5: [3, 4],
	6: [7],
	7: [2, 6, 8],
	8: [1, 7]
}

# T: All nodes and vertices are visited. Avg is O(V+E), for tree it's O(V)
def dfs_recursive(graph, n, visit):
	visit.add(n)
	print(n, end=' ')
	for nei in graph[n]:
		if nei not in visit:
			dfs_recursive(graph, nei, visit)
   
def dfs_recursive2(graph, n, visit):
    if n not in visit: 
        visit.add(n)
        print(n, end=' ')
        for nei in graph[n]:
            dfs_recursive2(graph, nei, visit)

def dfs_iterative(graph, root):
    visit = {root}
    stack = [root]
    
    while stack: 
        n = stack.pop() 
        print(n, end=' ')
        for nei in graph[n]:
            if nei not in visit: 
                visit.add(nei)
                stack.append(nei)
            
    

# dfs_recursive(graph, 1, set())
# print("")
# dfs_recursive(graph, 1, set())
# print("")
# dfs_iterative(graph, 1)
# print("")





from collections import deque 

def bfs(graph, start):
    q = deque([start])
    visit = {start}
    while q: 
        n = q.popleft() 
        print(n, end=' ')
        for nei in graph[n]:
            if nei not in visit: 
                visit.add(nei)
                q.append(nei)
         
    
bfs(graph,1)