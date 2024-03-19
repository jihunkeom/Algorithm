import sys

input = sys.stdin.readline

x, y, z = map(int, input().split())

result = {}

for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, z+1):
            tmp = i + j + k
            if tmp in result:
                result[tmp] += 1
            else:
                result[tmp] = 1
                
max_cnt = 0

for a, b in result.items():
    if b > max_cnt:
        max_cnt = b
        answer = a
        
print(answer)