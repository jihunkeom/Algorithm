import sys
import heapq

input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))
    
array.sort(key=lambda x: x[0])

heap = []

for x in array:
    heapq.heappush(heap, x[1])
    if len(heap) > x[0]:
        heapq.heappop(heap)
        
print(sum(heap))