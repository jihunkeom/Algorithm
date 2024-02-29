import sys

input = sys.stdin.readline

n = int(input())

graph = [0]
cards = list(range(1, n+1))
visited = [False] * (n+1)
visited2 = [False] * (n+1)

for _ in range(n):
    graph.append(int(input()))
    
    
def dfs(node):
    if not visited[node]:
        visited[node] = True
        
        next_node = graph[node]
        if not visited2[next_node]:
            visited2[next_node] = True
            dfs(next_node)
        
    
answer = []
for i in range(1, n+1):
    if i in answer:
        continue
    
    visited = [False] * (n+1)
    visited2 = [False] * (n+1)
    dfs(i)
    if visited == visited2:
        answer.append(str(i))
    # print(answer)
    # print("="*30)
    # print(i)
    # print(visited)
    # print(visited2)
    # print("="*30)
    
print(len(answer))
print("\n".join(answer))