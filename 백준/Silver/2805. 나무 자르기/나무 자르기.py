import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 0, max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for x in trees:
        if x > mid:
            total += (x - mid)
            
    if total >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)