import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
asc_arr = sorted(arr)
desc_arr = sorted(arr, reverse=True)

min_val = int(1e9)
for i in range(n):
    min_val = min(min_val, asc_arr[i] + desc_arr[i])
    
print(min_val)