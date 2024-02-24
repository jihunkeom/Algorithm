import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
computers = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    computers[b].append(a)
    
counts = [0] * (n+1)
max_cnt = 0
for x in range(1, n+1):
    visited = [0] * (n+1)
    count = 0
    queue = deque([x])
    visited[x] = 1
    
    while queue:
        pos = queue.popleft()
        count += 1
            
        for nx in computers[pos]:
            if visited[nx] == 0:
                queue.append(nx)
                visited[nx] = 1
                
    counts[x] = count
    if count > max_cnt:
        max_cnt = count
    
for i in range(1, n+1):
    if counts[i] == max_cnt:
        print(i, end=" ")