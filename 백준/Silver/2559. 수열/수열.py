import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().rstrip().split()))

temp = sum(arr[:k])
max_temp = temp

for i in range(1, n-k+1):
    # print(i, i+k-1)
    temp -= arr[i-1]
    temp += arr[i+k-1]
    
    if temp > max_temp:
        max_temp = temp
        
print(max_temp)