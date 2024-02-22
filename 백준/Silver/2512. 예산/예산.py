import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())

start = 0
end = max(arr)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += mid
        else:
            total += x
            
    if total > m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
        
print(answer)