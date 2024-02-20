import sys
from collections import deque

T = int(sys.stdin.readline())
answer = []
for _ in range(T):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    
    my_map = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    pos = []
    for _ in range(k):
        x, y = list(map(int, sys.stdin.readline().split()))
        my_map[x][y] = 1
        pos.append((x, y))
        
    if k == 1:
        answer.append(1)
        continue
        
    count = 0
    for x, y in pos:
        if not visited[x][y]:
            queue = deque()
            queue.append((x, y))
            while queue:
                cur_x, cur_y = queue.popleft()
                
                for nx, ny in ((cur_x+1, cur_y), (cur_x-1, cur_y), (cur_x, cur_y+1), (cur_x, cur_y-1)):
                    if (nx < 0) or (ny < 0) or (nx >= m) or (ny >= n):
                        continue
                    if visited[nx][ny]:
                        continue
                    
                    if my_map[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        
            count += 1
                
    answer.append(count)
    
for x in answer:
    print(x)