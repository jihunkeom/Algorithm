text1 = input()
text2 = input()

dp = [[0]*(len(text1)+1) for _ in range((len(text2)+1))]

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if text2[i-1] == text1[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])