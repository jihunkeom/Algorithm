n, s, m = map(int, input().split())
dp = [[False] * (m+1) for _ in range(n+1)]
dp[0][s] = True
sounds = list(map(int, input().split()))

for i in range(n):
    diff = sounds[i]
    for j in range(m+1):
        if dp[i][j] == True:
            if j-diff >= 0:
                dp[i+1][j-diff] = True
            if j+diff <= m:
                dp[i+1][j+diff] = True


answer = -1
for i in range(m, -1, -1):
    if dp[-1][i] == True:
        answer = i
        break

print(answer)