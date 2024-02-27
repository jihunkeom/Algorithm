import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

ans = 0

for i in range(n):
    tmp = nums[:i] + nums[i+1:]
    left, right = 0, len(tmp)-1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == nums[i]:
            ans += 1
            break
        if t < nums[i]:
            left += 1
        else:
            right -= 1
            
print(ans)