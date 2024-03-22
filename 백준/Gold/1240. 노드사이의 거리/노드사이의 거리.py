import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def find(graph, node, dist):
    for next_node, next_cost in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            cost = next_cost + dist
            distances[next_node] = cost
            find(graph, next_node, cost)

for _ in range(m):
    x, y = map(int, input().split())
    visited = [False] * (n+1)
    distances = [0] * (n+1)
    visited[x] = True
    find(graph, x, 0)
    print(distances[y])