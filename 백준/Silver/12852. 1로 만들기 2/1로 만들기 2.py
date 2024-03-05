n = int(input())
dp = [[0, []] for _ in range(n+1)]

dp[1][0] = 0
dp[1][1] = ["1"]

for x in range(2, n+1):
    dp[x] = [dp[x-1][0]+1, dp[x-1][1]+[str(x)]]
    
    if x % 2 == 0:
        tmp = dp[x//2][0] + 1
        if tmp < dp[x][0]:
            dp[x] = [tmp, dp[x//2][1] + [str(x)]]
            
    if x % 3 == 0:
        tmp = dp[x//3][0] + 1
        if tmp < dp[x][0]:
            dp[x] = [tmp, dp[x//3][1] + [str(x)]]

print(dp[-1][0])
print(" ".join(reversed(dp[-1][1])))