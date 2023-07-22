from collections import deque

m, n = map(int, input().split())

matrix = list()
for _ in range(n):
    x = list(input())
    matrix.append(list(map(int, x)))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[-1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0

def bfs():
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if x == (n-1) and y == (m-1):
            print(visited[x][y])
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if visited[nx][ny] == -1:
                    if matrix[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft((nx, ny))
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                        
bfs()