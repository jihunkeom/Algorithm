import sys

input = sys.stdin.readline

n = int(input())
meetings = []

if n == 1:
    print(1)
    sys.exit(0)

for _ in range(n):
    meetings.append(list(map(int, input().split())))
    
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
time = 0
for start, end in meetings:
    if start >= time:
        cnt += 1
        time = end
        
print(cnt)