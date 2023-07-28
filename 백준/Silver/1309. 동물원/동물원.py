n = int(input())

dp = [1, 1, 1]

for _ in range(2, n+1):
    tmp = [0, 0, 0]
    tmp[0] = sum(dp)
    tmp[1] = dp[0] + dp[2]
    tmp[2] = dp[0] + dp[1]
    dp = tmp
    
print(sum(dp) % 9901)