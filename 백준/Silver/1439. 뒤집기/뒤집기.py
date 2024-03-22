import sys

input = sys.stdin.readline

arr = list(map(int, input().rstrip()))

cnt0, cnt1 = 0, 0
cur = arr[0]
if cur == 0:
    cnt0 += 1
else:
    cnt1 += 1

for x in arr[1:]:
    if cur != x:
        cur = x
        if x == 0:
            cnt0 += 1
        else:
            cnt1 += 1
            
print(min(cnt0, cnt1))