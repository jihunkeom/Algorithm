import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())


graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visited = [[False] * (m) for _ in range(n)]
            visited[i][j] = True
            tmp = int(1e9)
            queue = deque([(i, j, 0)])
            
            while queue:
                x, y, cnt = queue.popleft()
                
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)):
                    if (nx < 0) or (nx >= n) or (ny < 0) or (ny >= m):
                        continue
                    
                    if not visited[nx][ny] and graph[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny, cnt+1))
                    elif graph[nx][ny] == 1:
                        if (cnt+1) < tmp:
                            tmp = cnt + 1
                            break
                        
            if tmp > answer:
                answer = tmp
                
print(answer)