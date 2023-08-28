import heapq

N, E = map(int, input().split())
graph = {}
for _ in range(E):
    a, b, c = map(int, input().split())
    if a not in graph:
        graph[a] = {b: c}
    else:
        if b not in graph[a]:
            graph[a].update({b: c})
        else:
            graph[a][b] = min(graph[a][b], c)
            
    if b not in graph:
        graph[b] = {a: c}
    else:
        if a not in graph[b]:
            graph[b].update({a: c})
        else:
            graph[b][a] = min(graph[b][a], c)
            
v1, v2 = map(int, input().split())

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    # all_paths = {node: [] for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        
        if cur_dist > distances[cur_node]:
            continue
        
        for adj, weight in graph[cur_node].items():
            dist = cur_dist + weight
            if dist < distances[adj]:
                distances[adj] = dist
                heapq.heappush(queue, [dist, adj])
                
    return distances
try:
    candidate1 = dijkstra(graph, 1)[v1] + dijkstra(graph, v1)[v2] + dijkstra(graph, v2)[N]
    candidate2 = dijkstra(graph, 1)[v2] + dijkstra(graph, v2)[v1] + dijkstra(graph, v1)[N]
    print(min(candidate1, candidate2))
except:
    print(-1)