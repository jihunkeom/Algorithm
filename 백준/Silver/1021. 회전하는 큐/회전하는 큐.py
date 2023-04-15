import sys
from collections import deque
input = sys.stdin.readline
n, idx = list(map(int, input().split()))
idx_list = list(map(int, input().split()))
dq = deque(list(range(1, n+1)))

cnt = 0
for i in idx_list:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                dq.append(dq.popleft())
                cnt += 1
            else:
                dq.appendleft(dq.pop())
                cnt += 1
                
print(cnt)