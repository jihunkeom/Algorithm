import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
answer = []
max_val, min_val = -int(1e9), int(1e9)

def find(idx, num, add, sub, mul, div):
    global max_val, min_val
    if idx == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return
    
    if add:
        find(idx + 1, num + nums[idx], add-1, sub, mul, div)
    if sub:
        find(idx + 1, num - nums[idx], add, sub-1, mul, div)
    if mul:
        find(idx + 1, num * nums[idx], add, sub, mul-1, div)
    if div:
        find(idx + 1, int(num / nums[idx]), add, sub, mul, div-1)
        
find(1, nums[0], add, sub, mul, div)
print(max_val)
print(min_val)