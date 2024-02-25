import sys

T = int(sys.stdin.readline())
for _ in range(T):
    key = sys.stdin.readline().rstrip()
    lstack, rstack = [], []
    
    for x in key:
        if x == "<":
            if lstack:
                rstack.append(lstack.pop(-1))
        elif x == ">":
            if rstack:
                lstack.append(rstack.pop(-1))
        elif x == "-":
            if lstack:
                lstack.pop(-1)
        else:
            lstack.append(x)
    
    answer = lstack + rstack[::-1]
    print("".join(answer))