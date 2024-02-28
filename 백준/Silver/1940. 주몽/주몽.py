import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = list(map(int, input().rstrip().split()))

arr.sort()

idx1, idx2 = 0, n-1
answer = 0
while idx1 < idx2:
    if arr[idx1] + arr[idx2] < m:
        idx1 += 1
    elif arr[idx1] + arr[idx2] > m:
        idx2 -= 1
    else:
        answer += 1
        idx1 += 1
        idx2 -= 1
        
print(answer)