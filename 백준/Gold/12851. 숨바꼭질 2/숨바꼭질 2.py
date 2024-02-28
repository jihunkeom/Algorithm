import sys
from collections import deque

input = sys.stdin.readline
INF = int(10**9)

n, k = map(int, input().rstrip().split())

visited = [INF] * (100001)
visited[n] = 0

queue = deque([n])
cnt = 0
answer = 0
while queue:
    pos = queue.popleft()
    
    if pos == k:
        cnt += 1
        
    for next_pos in (pos-1, pos+1, pos*2):
        if next_pos < 0 or next_pos > 100000:
            continue
        if visited[next_pos] >= (visited[pos] + 1):
            visited[next_pos] = visited[pos] + 1
            queue.append(next_pos)
            
print(visited[k])
print(cnt)