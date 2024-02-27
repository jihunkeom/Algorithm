import sys

input = sys.stdin.readline

line = input().rstrip()
m = int(input().rstrip())
coms = []
for _ in range(m):
    coms.append(input().rstrip().split())
    
lstack, rstack = [], []
lstack = [x for x in line]
for x in coms:
    if len(x) == 2:
        lstack.append(x[1])
    else:
        if x[0] == "L":
            if lstack:
                a = lstack.pop(-1)
                rstack.append(a)
        elif x[0] == "D":
            if rstack:
                a = rstack.pop(-1)
                lstack.append(a)
        elif x[0] == "B":
            if lstack:
                lstack.pop(-1)

lstack = lstack + rstack[::-1]

print("".join(lstack))