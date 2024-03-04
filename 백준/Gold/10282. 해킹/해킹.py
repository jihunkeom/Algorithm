import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for j in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))
    
    distances = [INF] * (n+1)
    queue = []
    heapq.heappush(queue, (0, c))
    distances[c] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        # print(distances, node, dist)
        if distances[node] > dist:
            continue
        
        for next_node, next_dist in graph[node]:
            # print("+", next_node, next_dist)
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
                
    tmp = [x for x in distances if x < INF]
    print(len(tmp), max(tmp))