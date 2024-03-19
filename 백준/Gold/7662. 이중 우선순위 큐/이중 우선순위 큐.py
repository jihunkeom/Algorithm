import sys
import heapq

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    min_queue = []
    max_queue = []
    k = int(input().rstrip())
    dropped = [False] * (k+1)
    
    for idx in range(k):
        op, num = input().rstrip().split()
        num = float(num)
        if op == "I":
            heapq.heappush(min_queue, (num, idx))
            heapq.heappush(max_queue, (-num, idx))
            
        elif op == "D":
            if num == 1:
                while True:
                    if not max_queue:
                        break
                    n, i = heapq.heappop(max_queue)
                    if not dropped[i]:
                        dropped[i] = True
                        break
            else:
                while True:
                    if not min_queue:
                        break
                    n, i = heapq.heappop(min_queue)
                    if not dropped[i]:
                        dropped[i] = True
                        break

    if max_queue and min_queue:
        flag = True
        while True:
            if not max_queue:
                flag = False
                break
            max_val, i = heapq.heappop(max_queue)
            if not dropped[i]:
                break
        while True:
            if not min_queue:
                flag = False
                break
            min_val, i = heapq.heappop(min_queue)
            if not dropped[i]:
                break
    else:
        flag = False
        
    if flag:
        print(int(-max_val), int(min_val))
    else:
        print("EMPTY")