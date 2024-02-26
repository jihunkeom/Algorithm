import sys
import heapq

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    
    nums = list(map(int, sys.stdin.readline().split()))
    
    for num in nums:
        if len(arr) < n:
            heapq.heappush(arr, num)
        
        else:
            if num > arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr, num)
                
print(arr[0])