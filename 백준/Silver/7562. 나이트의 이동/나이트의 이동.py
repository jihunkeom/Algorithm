from collections import deque

def bfs(dist, start, goal):
    queue = deque([start])
    while queue:
        cur_x, cur_y = queue.popleft()
        if (cur_x == goal[0]) and (cur_y == goal[1]):
            print(dist[cur_x][cur_y])
            break
        
        for next_x, next_y in ([cur_x+2, cur_y+1], [cur_x+2, cur_y-1], [cur_x+1, cur_y+2], [cur_x+1, cur_y-2], [cur_x-2, cur_y+1], [cur_x-2, cur_y-1], [cur_x-1, cur_y+2], [cur_x-1, cur_y-2]):
            if (0 <= next_x < i) and (0 <= next_y < i):
                if dist[next_x][next_y] == -1:
                    queue.append([next_x, next_y])
                    dist[next_x][next_y] = dist[cur_x][cur_y] + 1            

t = int(input())

for _ in range(t):
    i = int(input())
    start = list(map(int, input().strip().split()))
    goal = list(map(int, input().strip().split()))
    
    dist = [[-1 for _ in range(i)] for _ in range(i)]
    dist[start[0]][start[1]] = 0
    bfs(dist, start, goal)