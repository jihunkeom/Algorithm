import sys
sys.setrecursionlimit(10**6)
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
        parents[y] = x
    else:
        parents[x] = y
        
    return None

parents = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    find(i)

print(len(set(parents[1:])))