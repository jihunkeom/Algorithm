import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

computers = [[] for _ in range(n+1)]
viruses = []
visited = [False] * (n+1)

for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    computers[a].append(b)
    computers[b].append(a)
    
def dfs(x):
    if not visited[x]:
        visited[x] = True
        viruses.append(x)
        
        for nx in computers[x]:
            if not visited[nx]:
                dfs(nx)
                
dfs(1)
print(len(viruses)-1)