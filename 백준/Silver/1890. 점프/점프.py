import sys
input = sys.stdin.readline
n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            if x + graph[x][y] < n:
                dp[x + graph[x][y]][y] += dp[x][y]
            if y + graph[x][y] < n:
                dp[x][y + graph[x][y]] += dp[x][y]
                
print(dp[-1][-1])