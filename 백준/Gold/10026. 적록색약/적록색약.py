import sys
from collections import deque

n = int(input())
map = list()

for _ in range(n):
    x = sys.stdin.readline().strip()
    map.append(list(x))

def bfs(map, start, who):
    flag = False
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        color = map[r][c]
        for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if (0 <= next_r < n) and (0 <= next_c < n):
                if who == 1:
                    flag = not visited[next_r][next_c] and color == map[next_r][next_c]
                else:
                    flag = not visited[next_r][next_c] and ((color in ["R", "G"] and map[next_r][next_c] in ["R", "G"]) or (color == "B" and map[next_r][next_c] == "B"))
                    
                
                if flag:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))
    return map

cnt1 = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    while not all(visited[i]):
        start = (i, visited[i].index(False))
        visited[start[0]][start[1]] = True
        map = bfs(map, start, 1)
        cnt1 += 1

cnt2 = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    while not all(visited[i]):
        start = (i, visited[i].index(False))
        visited[start[0]][start[1]] = True
        map = bfs(map, start, 2)
        cnt2 += 1

print(cnt1, cnt2)