import sys

n, m = list(map(int, sys.stdin.readline().split()))
lectures = list(map(int, sys.stdin.readline().split()))

start, end = max(lectures), sum(lectures)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    total = 0
    
    for x in lectures:
        if total + x > mid:
            cnt += 1
            total = x
        else:
            total += x
            
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
        
print(answer)