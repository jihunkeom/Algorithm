import sys

input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    a, b = input().split()
    array.append((int(a), b))
    
array.sort(key=lambda x: x[0])

for x in array:
    print(x[0], x[1])