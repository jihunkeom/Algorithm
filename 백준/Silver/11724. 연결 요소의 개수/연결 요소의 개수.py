import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m = list(map(int, sys.stdin.readline().split()))

my_map = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    my_map[a].append(b)
    my_map[b].append(a)
    
def dfs(node):
    for next_node in my_map[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)
            
    return 1

cc = 0
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        cc += dfs(i)
        
print(cc)