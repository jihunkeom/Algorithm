import sys
input = sys.stdin.readline
n = int(input())

count = 1
stack = []
result = []

for _ in range(n):
    num = int(input())
    while num >= count:
        stack.append(count)
        count += 1
        result.append("+")
        
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        result=["NO"]
        break

print("\n".join(result))