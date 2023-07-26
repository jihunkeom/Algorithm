n = int(input())

dp = {1: 0, 2: 1, 3: 1}
for i in range(4, n+1):
    candidates = [dp[i-1] + 1]
    if i % 3 == 0:
        candidates.append(dp[i//3] + 1)
    if i % 2 == 0:
        candidates.append(dp[i//2] + 1)
    
    dp[i] = min(candidates)
        
print(dp[n])