import heapq

n = int(input())
m = int(input())
bus = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if a not in bus:
        bus[a] = {b: c}
    else:
        if b not in bus[a]:
            bus[a].update({b: c})
        else:
            bus[a][b] = min(bus[a][b], c)
            
for i in range(1, n+1):
    if i not in bus:
        bus[i] = {}
            
start, end = map(int, input().split())

def dijkstra(graph, start, end):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    all_paths = {node: [] for node in graph}
    queue = []
    heapq.heappush(queue, [distances[start], start, [start]])
    
    while queue:
        current_dist, current_node, path = heapq.heappop(queue)
        
        if current_dist > distances[current_node]:
            continue
        
        for adj, weight in graph[current_node].items():
            dist = current_dist + weight
            if dist < distances[adj]:
                new_path = path + [adj]
                distances[adj] = dist
                heapq.heappush(queue, [dist, adj, new_path])
                all_paths[adj] = new_path
    return distances, all_paths
    
dist, all_paths = dijkstra(bus, start, end)

path = [str(x) for x in all_paths[end]]
print(dist[end])
print(len(path))
print(" ".join(path))