from collections import deque

m, n = map(int, input().split())
map = []
for _ in range(n):
    map.append(list(input()))

visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(start):
    queue = deque([start])
    cnt = 1
    team = map[start[0]][start[1]]
    while queue:
        r, c = queue.popleft()

        for next_r, next_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if (0 <= next_r < n) and (0 <= next_c < m):
                if not visited[next_r][next_c] and team == map[next_r][next_c]:
                    cnt += 1
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))

    return cnt**2

team1, team2 = 0, 0
for i in range(n):
    while not all(visited[i]):
        pos = visited[i].index(False)
        visited[i][pos] = True
        power = bfs((i, pos))
        if map[i][pos] == "W":
            team1 += power
        else:
            team2 += power

print(team1, team2)