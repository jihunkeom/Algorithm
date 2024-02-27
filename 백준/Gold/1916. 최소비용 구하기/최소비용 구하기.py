import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
start, target = map(int, input().split())

all_costs = [INF] * (n+1)
all_costs[start] = 0

queue = []
heapq.heappush(queue, (0, start))
while queue:
    current_cost, current_city = heapq.heappop(queue)
    
    if current_cost > all_costs[current_city]:
        continue
    
    for next_city, next_cost in graph[current_city]:
        total_cost = current_cost + next_cost
        if total_cost < all_costs[next_city]:
            all_costs[next_city] = total_cost
            heapq.heappush(queue, (total_cost, next_city))
            
print(all_costs[target])