dp = [0] * 101
dp[:10] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(9, n):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n-1])