import sys

input = sys.stdin.readline

n, l = map(int, input().split())
info = []

for _ in range(n):
    info.append(list(map(int, input().split())))
    
info.sort(key=lambda x: x[0])

answer = 0

for i in range(n):
    q, r = divmod(info[i][1] - info[i][0], l)
    if r == 0:
        answer += q
    else:
        # print(info[i], r, l, info[i+1])
        if i < n-1:
            if (info[i][1] - r + l > info[i+1][0]) and i < n-1:
                info[i+1][0] = info[i][0]
            else:
                answer += q+1
        else:
            answer += q+1
            
print(answer)