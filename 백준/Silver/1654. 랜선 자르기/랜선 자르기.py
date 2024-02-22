import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

lans = []
for _ in range(n):
    lans.append(int(sys.stdin.readline().rstrip()))
    
start, end = 1, max(lans)

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for x in lans:
        if x >= mid and mid > 0:
            total += x // mid
            
    if total >= k:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
        
print(answer)