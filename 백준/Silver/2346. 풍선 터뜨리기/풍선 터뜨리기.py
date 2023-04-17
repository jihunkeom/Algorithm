import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
moves = list(map(int, input().split()))
queue = deque([(i, moves[i-1]) for i in range(1, len(moves)+1)])
answer = []

x = queue.popleft()
answer.append(x[0])
for i in range(N-1):
    if x[1] > 0:
        for j in range(x[1]-1):
            queue.append(queue.popleft())
    else:
        for j in range(-x[1]):
            queue.appendleft(queue.pop())
            
    x = queue.popleft()
    answer.append(x[0])
    
for x in answer:
    print(x, end=" ")