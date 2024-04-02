import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = set()
for _ in range(n):
    arr.add(input().rstrip())
    
    
answer = n
for _ in range(m):
    tmp = input().rstrip().split(",")
    for x in tmp:
        arr.discard(x)
    print(len(arr))