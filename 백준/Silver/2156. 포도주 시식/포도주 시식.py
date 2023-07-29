n = int(input())
wines = []
for _ in range(n):
    wines.append(int(input()))

if len(wines) < 3:
    print(sum(wines))
else:
    dp = [wines[0], wines[0]+wines[1]] + [0]*(len(wines)-2)
    for i in range(2, len(wines)):
        dp[i] = (max(dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i], dp[i-1]))

    print(dp[-1])