from collections import deque

def solution(maps):
    answer = 0
    
    queue = deque()
    queue.append((0, 0))
    reach = False
    
    while queue:
        x, y = queue.popleft()
        if x == len(maps)-1 and y == len(maps[0])-1:
            reach = True
        
        for nx, ny in ((x, y+1), (x, y-1), (x-1, y), (x+1, y)):
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
                
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    if reach:
        return maps[-1][-1]
    
    return -1