import sys
import heapq
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    heap_data = []
    heapq.heappush(heap_data, (0, s))
    distances[s] = 0
    while heap_data:
        dist, node = heapq.heappop(heap_data)
        if dist > distances[node]:
            continue
        
        for nx in graph[node]:
            cost = dist + nx[1]
            if cost < distances[nx[0]] and not best_path[node][nx[0]]:
                distances[nx[0]] = cost
                heapq.heappush(heap_data, (cost, nx[0]))
                
def bfs():
    queue = deque()
    queue.append(d)
    
    while queue:
        node = queue.popleft()
        
        for nx in reverse_graph[node]:
            if nx[1] + distances[nx[0]] == distances[node] and not visited[node][nx[0]]:
                best_path[nx[0]][node] = True
                visited[node][nx[0]] = True
                queue.append(nx[0])
    
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split())
    
    
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    distances = [INF] * n
    best_path = [[False] * (n) for _ in range(n)]
    visited = [[False] * (n) for _ in range(n)]
    
    for _ in range(m):
        u, v, p = map(int, input().split())
        
        graph[u].append((v, p))
        reverse_graph[v].append((u, p))
        
    dijkstra()
    
    bfs()
    distances = [INF] * n
    dijkstra()
    
    answer = distances[d]
    if answer < INF:
        print(answer)
    else:
        print(-1)