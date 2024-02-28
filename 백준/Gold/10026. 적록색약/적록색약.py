import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
map1 = []
for _ in range(n):
    map1.append([x for x in input().rstrip()])

def dfs1(x, y):
    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if (nx < 0) or (ny < 0) or (nx >= len(map1)) or (ny >= len(map1[0])):
            continue
        if visited[nx][ny] == False and map1[nx][ny] == map1[x][y]:
            visited[nx][ny] = True
            dfs1(nx, ny)
    return None

def dfs2(x, y):
    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if (nx < 0) or (ny < 0) or (nx >= len(map1)) or (ny >= len(map1[0])):
            continue
        if visited[nx][ny] == False:
            if (map1[nx][ny] in ["R", "G"] and map1[x][y] in ["R", "G"]) or (map1[nx][ny] == map1[x][y]):
                visited[nx][ny] = True
                dfs2(nx, ny)
    return None

visited = [[False] * n for _ in range(n)]
answer1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True
            dfs1(i, j)
            answer1 += 1
            
visited = [[False] * n for _ in range(n)]
answer2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True
            dfs2(i, j)
            answer2 += 1
            
print(answer1, answer2)