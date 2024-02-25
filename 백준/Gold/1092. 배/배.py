import sys

n = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().rstrip().split()))

cranes = sorted(cranes, reverse=True)
boxes = sorted(boxes, reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
else:
    result = 0
    positions = [0] * n
    moved = [False] * m
    count = 0
    while True:
        if count >= m:
            break
        
        for i in range(n):
            while positions[i] < m:
                if not moved[positions[i]] and cranes[i] >= boxes[positions[i]]:
                    moved[positions[i]] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        result += 1
        
    print(result)