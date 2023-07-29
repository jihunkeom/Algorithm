n = int(input())
houses = []
for _ in range(n):
    houses.append(list(map(int, input().split())))

dp = houses[0]
for i in range(1, n):
    tmp = [0, 0, 0]
    tmp[0] = min(dp[1] + houses[i][0], dp[2] + houses[i][0])
    tmp[1] = min(dp[0] + houses[i][1], dp[2] + houses[i][1])
    tmp[2] = min(dp[0] + houses[i][2], dp[1] + houses[i][2])
    dp = tmp

print(min(dp))