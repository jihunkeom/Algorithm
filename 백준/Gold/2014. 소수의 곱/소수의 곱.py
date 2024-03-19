import sys
import heapq

input = sys.stdin.readline

k, n = map(int, input().split())

nums = list(map(int, input().split()))
max_val = max(nums)
queue = []
tmp = set(nums[:])

for x in nums:
    heapq.heappush(queue, x)
    
for _ in range(n):
    a = heapq.heappop(queue)
        
    for x in nums:
        now = a * x
        
        if len(queue) >= n and max_val < now:
            continue
        if now not in tmp:
            heapq.heappush(queue, now)
            max_val = max(max_val, now)
            tmp.add(now)
        
print(a)