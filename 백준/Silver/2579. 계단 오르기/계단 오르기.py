import sys

n = int(sys.stdin.readline())
stairs = []
dp = [0] * (n)
for _ in range(n):
    tmp = int(sys.stdin.readline())
    stairs.append(tmp)

if n < 3:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    for i in range(2, n):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
    print(dp[-1])