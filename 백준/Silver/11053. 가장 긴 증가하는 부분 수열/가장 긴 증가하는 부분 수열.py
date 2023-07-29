n = int(input())
seq = list(map(int, input().split()))
arr = [1] * n

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            arr[i] = max(arr[i], arr[j]+1)

print(max(arr))