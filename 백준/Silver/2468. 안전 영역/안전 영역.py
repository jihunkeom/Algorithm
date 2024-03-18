import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
max_height = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    max_height = max(max_height, max(tmp))
    
answer = 0

for x in range(max_height+1):
    new_graph = []
    for i in range(n):
        new_graph.append([1 if graph[i][j] > x else 0 for j in range(n)])
    
    queue = deque()
    visited = [[False] * (n) for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if new_graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j))
                cnt += 1
                while queue:
                    cur_x, cur_y = queue.popleft()
                    
                    for nx, ny in ((cur_x+1, cur_y), (cur_x-1, cur_y), (cur_x, cur_y+1), (cur_x, cur_y-1)):
                        if (nx < 0) or (ny < 0) or (nx >= n) or (ny >= n):
                            continue
                        
                        if not visited[nx][ny] and new_graph[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    
    answer = max(cnt, answer)
    
print(answer)