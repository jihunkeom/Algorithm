import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
dp = arr[:]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]+arr[i]:
            dp[i] = arr[i] + dp[j]
            
print(max(dp))