import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
pos = []
for i in range(n):
    tmp = list(input().rstrip())
    board.append(tmp)
    
    loc = [i for i, val in enumerate(tmp) if val == "o"]
    for x in loc:
        pos.append((i, x))
    
def out(pos):
    if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= m:
        return True
    else:
        return False
    
queue = deque()
queue.append((pos[0], pos[1], 0))
min_cnt = int(1e9)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visisted = set()

while queue:
    pos1, pos2, cnt = queue.popleft()
    out1, out2 = out(pos1), out(pos2)
        
    if out1 and not out2:
        min_cnt = min(cnt, min_cnt)
        continue
    elif out2 and not out1:
        min_cnt = min(cnt, min_cnt)
        continue
    elif out1 and out2:
        continue
    
    if cnt >= 10:
        continue
    
    for i in range(4):
        n_pos1 = (pos1[0]+dx[i], pos1[1]+dy[i])
        n_pos2 = (pos2[0]+dx[i], pos2[1]+dy[i])
        out1, out2 = out(n_pos1), out(n_pos2)

        if out1 and not out2:
            min_cnt = min(cnt+1, min_cnt)
            continue
        elif out2 and not out1:
            min_cnt = min(cnt+1, min_cnt)
            continue
        elif out1 and out2:
            continue
        
        if board[n_pos1[0]][n_pos1[1]] == "#":
            n_pos1 = pos1
        if board[n_pos2[0]][n_pos2[1]] == "#":
            n_pos2 = pos2
        
        if (n_pos1, n_pos2) not in visisted:
            queue.append((n_pos1, n_pos2, cnt+1))
            visisted.add((n_pos1, n_pos2))
        
if min_cnt < int(1e9):
    print(min_cnt)
else:
    print(-1)