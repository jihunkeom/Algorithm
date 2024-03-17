import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    distances = [INF] * (n+1)
    for _ in range(d):
        x, y, z = map(int, input().split())
        graph[y].append((x, z))
        
    heap_data = []
    heapq.heappush(heap_data, (0, c))
    distances[c] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        
        if dist > distances[now]:
            continue
        
        for a, b in graph[now]:
            cost = b + distances[now]
            
            if cost < distances[a]:
                distances[a] = cost
                heapq.heappush(heap_data, (cost, a))
                
    answer_1 = 0
    answer_2 = 0
    for x in distances[1:]:
        if x < INF:
            answer_1 += 1

            answer_2 = max(answer_2, x)
    
    print(answer_1, answer_2)
