from collections import deque

n, k = map(int, input().split())

MAX = 100001
visited = [-1] * MAX
visited[n] = 0
path = dict()

def bfs():
    queue = deque([n])
    while queue:
        cur = queue.popleft()
        if cur == k:
            print(visited[cur])
            break

        for next_pos in [cur-1, cur+1, cur*2]:
            if 0 <= next_pos < MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[cur] + 1
                queue.append(next_pos)
                path[next_pos] = cur

bfs()
answer = [str(k)]
while k in path.keys():
    answer.append(str(path[k]))
    k = path[k]
print(" ".join(answer[::-1]))