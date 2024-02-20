import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [-1000] * (n)
dp[0] = arr[0]
for i in range(1, n):
    tmp = arr[i] + dp[i-1]
    if tmp > arr[i] and dp[i-1]:
        dp[i] = tmp
    else:
        dp[i] = arr[i]

    
print(max(dp))