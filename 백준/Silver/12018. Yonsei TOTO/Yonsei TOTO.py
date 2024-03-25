import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    p, l = map(int, input().split())
    tmp = list(map(int, input().split()))
    
    if len(tmp) < l:
        arr.append(1)
    else:
        tmp.sort(reverse=True)
        arr.append(tmp[l-1])
        
        
arr.sort()
cnt = 0
for x in arr:
    if m >= x:
        m -= x
        cnt += 1
    if m < x:
        break
print(cnt)