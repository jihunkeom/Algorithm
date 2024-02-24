import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1):
    graph[i] = sorted(graph[i])

dfs_order = []
visited = [False] * (N+1)
def dfs(v):    
    visited[v] = True
    dfs_order.append(str(v))
    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            dfs(next)

dfs(V)
print(" ".join(dfs_order).rstrip())

visited = [False] * (N+1)
bfs_order = []
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        bfs_order.append(str(x))
        
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
                
bfs(V)
print(" ".join(bfs_order).rstrip())