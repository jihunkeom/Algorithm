from collections import deque

N, M = list(map(int, input().split()))
queue = deque(list(range(1, N+1)))
answer = []
while queue:
    for _ in range(M-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
    
print("<", end="")
for i in range(len(answer)):
    if i == len(answer)-1:
        print(answer[i], end="")
    else:
        print(answer[i], end=", ")
print(">", end="")