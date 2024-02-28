import sys

input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 1
while b > a:
    temp = b
    
    if b % 2 == 0:
        b = b // 2
        cnt += 1
    elif b % 10 == 1:
        b = b // 10
        cnt += 1
    else:
        break
        
        
        
if b==a:
    print(cnt)
else:
    print(-1)