import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))


cnt = 1
visit = sum(arr[:x])
max_visitor = visit

for i in range(1, n-x+1):
    # print(i, arr)
    # print(arr[i], arr[i+x-1])
    # print(visit, max_visitor)
    visit -= arr[i-1]
    visit += arr[i+x-1]
    
    if visit > max_visitor:
        cnt = 1
        max_visitor = visit
    elif visit == max_visitor:
        cnt += 1
        
    
if max_visitor > 0:
    print(max_visitor)
    print(cnt)
else:
    print("SAD")