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
