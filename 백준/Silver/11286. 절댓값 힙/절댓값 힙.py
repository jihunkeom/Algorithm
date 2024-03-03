import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])