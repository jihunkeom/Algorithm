import sys
input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    x = input().split()
    cmd = x[0]
    if cmd == "push":
        stack.append(int(x[1]))
    elif cmd == "pop":
        if len(stack) > 0:
            popped = stack.pop()
            print(popped)
        else:
            print(-1)
    elif cmd == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)