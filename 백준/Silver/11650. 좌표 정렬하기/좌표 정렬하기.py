import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
    
array.sort(key=lambda x: (x[0], x[1]))

for x in array:
    print(x[0], x[1])