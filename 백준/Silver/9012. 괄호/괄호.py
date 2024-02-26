import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    ps = sys.stdin.readline().rstrip()
    
    stack = [ps[0]]
    for x in ps[1:]:
        if len(stack) > 0 and stack[-1] == "(" and x == ")":
            stack.pop(-1)
        else:
            stack.append(x)
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")