import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num < 0:
        heapq.heappush(heap, (-num, num))
    elif num > 0:
        heapq.heappush(heap, (num, num))
    elif heap:
        a = heapq.heappop(heap)
        print(a[1])
    else:
        print(0)
