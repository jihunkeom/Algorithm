import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    connected = list(map(int, input().split()))
    for j in range(n):
        if connected[j] == 1:
            graph[i].append(j)

# dfs            
def dfs(node):    
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node)
    
for i in range(n):
    visited = [0] * n
    dfs(i)
    print(" ".join([str(x) for x in visited]))