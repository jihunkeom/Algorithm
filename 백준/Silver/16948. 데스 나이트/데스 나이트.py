from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().strip().split())

board = [[-1 for _ in range(n)] for _ in range(n)]
board[r1][c1] = 0

def bfs():
    success = False
    queue = deque([(r1, c1)])
    while queue:
        r, c = queue.popleft()
        if r == r2 and c == c2:
            print(board[r][c])
            success = True
            break
        
        for next_r, next_c in [(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)]:
            if (0 <= next_r < n) and (0 <= next_c < n) and board[next_r][next_c] == -1:
                board[next_r][next_c] = board[r][c] + 1
                queue.append((next_r, next_c))
            
    if not success:
        print(-1)
    
bfs()