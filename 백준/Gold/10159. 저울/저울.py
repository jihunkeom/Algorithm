import sys
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph1 = [[INF] * (n+1) for _ in range(n+1)]
graph2 = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph1[i][i] = 0
    graph2[i][i] = 0
    
for _ in range(m):
    a, b = map(int, input().split())
    graph1[a][b] = 1
    graph2[b][a] = 1
    
for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph1[x][y] = min(graph1[x][y], graph1[x][k] + graph1[k][y])
            graph2[x][y] = min(graph2[x][y], graph2[x][k] + graph2[k][y])
            
            
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph1[i][j] == INF and graph2[i][j] == INF:
            cnt += 1
        
    print(cnt)