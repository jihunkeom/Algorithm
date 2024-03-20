import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m = map(int, input().split())

def find(x):
    if parents[x] == x:
        return x
    else:
        tmp = find(parents[x])
        parents[x] = tmp
        return tmp

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parents[y] = parents[x]
    else:
        parents[x] = parents[y]

flag = False
answer = 0
parents = [i for i in range(n)]
for idx in range(m):
    a, b = map(int, input().split())
    
    if not flag and find(a) == find(b):
        flag = True
        answer = idx + 1
        
    union(a, b)
    
print(answer)