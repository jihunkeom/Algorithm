import sys

input = sys.stdin.readline

dp = [1] * 1001
for i in range(1, 1001):
    dp[i] = dp[i-1] * i

n, k = map(int, input().split())

print(dp[n] // (dp[n-k] * dp[k]) % 10007)