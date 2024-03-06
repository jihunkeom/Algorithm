import sys

input = sys.stdin.readline

n = int(input())
health = 0

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dp = [[0] * (101) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if j <= arr1[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-arr1[i-1]] + arr2[i-1], dp[i-1][j])
            
print(dp[-1][-1])