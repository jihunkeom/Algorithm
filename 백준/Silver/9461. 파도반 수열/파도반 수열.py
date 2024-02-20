import sys

T = int(sys.stdin.readline())
dp = [0] * 101
for _ in range(T):
    N = int(sys.stdin.readline())
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, N+1):
        dp[i] = dp[i-2] + dp[i-3]
        
    print(dp[N])