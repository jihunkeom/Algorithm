import sys

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

answer = -1

idx1, idx2 = 0, 0
tmp = arr[0]
answer = 100001

while idx1 <= idx2:
    # print(tmp, idx1, idx2)
    if tmp < s:
        idx2 += 1
        if idx2 >= n:
            break
        tmp += arr[idx2]
    elif tmp >= s:
        if (idx2 - idx1 + 1) < answer:
            answer = (idx2 - idx1 + 1)
            # print("="*30)
            # print(tmp, answer, idx1, idx2)
            # print("="*30)
        tmp -= arr[idx1]
        idx1 += 1
        
if answer < 100001:
    print(answer)
else:
    print(0)