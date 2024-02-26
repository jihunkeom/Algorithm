import sys
import heapq

N = int(sys.stdin.readline())

my_list = []
for _ in range(N):
    op = int(sys.stdin.readline())
    if op == 0:
        if len(my_list) > 0:
            a = heapq.heappop(my_list)
            print(a)
        else:
            print(0)
    else:
        heapq.heappush(my_list, op)