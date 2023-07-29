import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+nums[i], 0)

if max(dp) > 0:
    print(max(dp))
else:
    print(max(nums))