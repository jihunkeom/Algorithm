import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * n
dp[0] = "SK"
if n > 1:
    dp[1] = "CY"
if n > 2:
    dp[2] = "SK"
if n > 3:
    for i in range(3, n):
        if dp[i-1] == "SK":
            dp[i] = "CY"
        else:
            dp[i] = "SK"
        
        
print(dp[-1])