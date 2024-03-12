import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))
    
queue = deque([])
visited = [[False] * (n) for _ in range(n)]

answer = 0
cnts = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and not visited[i][j]:
            cnt = 1
            visited[i][j] = True
            
            queue.append((i, j))
            
            while queue:
                x, y = queue.popleft()
                
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    
                    if not visited[nx][ny] and graph[nx][ny] == "1":
                        visited[nx][ny] = True
                        cnt += 1
                        
                        queue.append((nx, ny))
            
            answer += 1
            cnts.append(cnt)
            
print(answer)
for x in sorted(cnts):
    print(x)