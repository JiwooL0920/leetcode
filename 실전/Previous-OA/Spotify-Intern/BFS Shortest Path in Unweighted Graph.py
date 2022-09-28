from collections import deque 

def shortestPath(graph, start, goal):
        visit = []
        q = deque([[start]])
        if start == goal:
            return "Same Node"
        while q:
            path = q.popleft()
            n = path[-1]
            if n not in visit:
                for neighbour in graph[n]:
                    newPath = list(path)
                    newPath.append(neighbour)
                    q.append(newPath)
                    if neighbour == goal:
                        return newPath
                    visit.append(n)
                
        return []


graph = {1: [2,4], 2: [1,3], 3: [2,4,7], 4: [1,3,5], 5: [4,8], 6: [7], 7: [3,6], 8: [5], 9: [10], 10: [9]}
print(shortestPath(graph, 1, 8))
print(shortestPath(graph, 1, 10))