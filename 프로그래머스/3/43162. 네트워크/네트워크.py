from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            queue = deque()
            queue.append(i)
            while queue:
                com = queue.popleft()
                for j in range(n):
                    if computers[com][j] == 1:
                        if not visited[j]:
                            visited[j] = True
                            queue.append(j)
            answer += 1
    
    return answer