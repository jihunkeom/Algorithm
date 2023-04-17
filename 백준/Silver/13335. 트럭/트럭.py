import sys
from collections import deque
input = sys.stdin.readline
n, w, l = list(map(int, input().split()))
trucks = deque(list(map(int, input().split())))
answer = 0
bridge = deque([])

while trucks:
    answer += 1
    if len(bridge) == w:
        x = bridge.popleft()
    
    if sum(bridge)+trucks[0] <= l:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)
    
print(answer+w)