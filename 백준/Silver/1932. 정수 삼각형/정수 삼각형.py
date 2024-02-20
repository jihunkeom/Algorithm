import sys

n = int(sys.stdin.readline())

dp = []
triangle = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    dp.append(tmp + [0] * (n - len(tmp)))
    triangle.append(tmp + [0] * (n - len(tmp)))
    

for i in range(len(dp)-1):
    for j in range(len(dp[0])-1):
        triangle[i+1][j] = max(triangle[i+1][j], dp[i+1][j] + triangle[i][j])
        triangle[i+1][j+1] = max(triangle[i+1][j+1], dp[i+1][j+1] + triangle[i][j])
        
print(max(triangle[-1]))