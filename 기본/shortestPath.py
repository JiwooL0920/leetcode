from collections import defaultdict

graph = {
    1: [(2,2), (4,1), (3,5)], # from : list of [to, distance]
    2: [(3,3), (4,2)],
    3: [(2,3), (6,5)],
    4: [(3,3), (5,1)],
    5: [(3,1), (6,2)],
    6: []    
}



def dijkstra(graph, start):
    # 데이타 설정 
    visit = set() 
    distance = {}
    for node in graph: 
        distance[node] = float("inf")
    n = len(graph)
    
    # 헬퍼 함수 - 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환 
    def get_smallest_node():
        min_value = float("inf")
        index = 0 #가장 최단 거리가 짧은 노드의 인덱스 
        for i in range(1, n+1):
            if distance[i] < min_value and i not in visit:
                min_value = distance[i]
                index = i 
        return index 
        
    # 시작 노드 초기화 
    distance[start] = 0
    visit.add(start)
    for nei, d in graph[start]:
        distance[nei] = d 
        
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복 
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리 
        now = get_smallest_node()
        visit.add(now)
        # 현재 노드와 연결된 다른 노드를 확인 
        for nei, d in graph[now]:
            cost = distance[now] + d 
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은경우 
            if cost < distance[nei]:
                distance[nei] = cost 
                
    # 모든 노드로 가기 위한 최단 거리를 출력: 
    for nei, d in distance.items():
        if d == float("inf"):
            # 도달할수없는 경우 
            print("node:", nei, "| distance:inf")
        else:
            print("node:", nei, "| distance:", d)
            
            
dijkstra(graph, 1)
        
        
    
################################3
# minheap 사용
import heapq #minheap

# heap sort (increasing order)
def heapsort_incr(arr):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삼입
    for value in arr:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result 

def heapsort_decr(arr):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삼입
    for value in arr:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result 

result1 = heapsort_incr([1,3,5,7,9,2,4,6,8,0])
print(result1)
result2 = heapsort_decr([1,3,5,7,9,2,4,6,8,0])
print(result2)



def dijkstra_heap(graph, start):
    # 데이타 설정 
    distance = {}
    for node in graph: 
        distance[node] = float("inf")
    
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여 큐에 삽입 
    heapq.heappush(q, (0, start))
    distance[start] = 0 
    
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        dist, now = heapq.heappop(q) 
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 
        if distance[now] < dist: 
            continue 
        # 현재 노드와 연결된 다른 인접한 노드들을 확인:
        for nei, d in graph[now]:
            cost = dist + d 
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nei]:
                distance[nei] = cost 
                heapq.heappush(q, (cost, nei))
    
    # 모든 노드로 가기 위한 최단 거리를 출력: 
    for nei, d in distance.items():
        if d == float("inf"):
            # 도달할수없는 경우 
            print("node:", nei, "| distance:inf")
        else:
            print("node:", nei, "| distance:", d)
    
dijkstra_heap(graph, 1)