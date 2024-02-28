import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque(list(range(1, n+1)))
cnt = 0

for x in arr:
    q, r = divmod(len(queue), 2)
    if queue.index(x)+1 <= (q+1):
        while queue[0] != x:
            queue.append(queue.popleft())
            cnt += 1
    else:
        while queue[0] != x:
            queue.appendleft(queue.pop())
            cnt += 1
    queue.popleft()
    
        
print(cnt)