import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
arr = list(input().rstrip())

dp = [INF] * (n)

dp[0] = 0

for i in range(1, n):
    if arr[i] == "B":
        check = "J"
    elif arr[i] == "O":
        check = "B"
    else:
        check = "O"
    
    for j in range(i):
        if arr[j] == check:
            dp[i] = min(dp[i], dp[j] + (i-j)**2)
            
if dp[-1] < INF:
    print(dp[-1])
else:
    print(-1)