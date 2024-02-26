import sys

N = int(sys.stdin.readline().rstrip())
times = list(map(int, sys.stdin.readline().rstrip().split()))

times = sorted(times)

answer = 0
cur_time = 0
for x in times:
    cur_time += x
    answer += cur_time

    
print(answer)