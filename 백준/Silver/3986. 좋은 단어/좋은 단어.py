import sys

n = int(sys.stdin.readline().rstrip())
lines = [sys.stdin.readline().rstrip() for _ in range(n)]

answer = 0
for line in lines:
    stack = [line[0]]
    for x in line[1:]:
        if len(stack) > 0 and x == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(x)
        
    if len(stack) == 0:
        answer += 1
        
print(answer)