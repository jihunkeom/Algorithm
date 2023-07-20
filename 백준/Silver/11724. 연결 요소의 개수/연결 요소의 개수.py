from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(start):
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        
        if not visited[cur]:
            visited[cur] = True
            queue.extend(adj[cur])
    return 1

visited = [True] + ([False] * n)
answer = 0
while not all(visited):
    start_node = visited.index(False)
    answer += bfs(start_node)
    
print(answer)