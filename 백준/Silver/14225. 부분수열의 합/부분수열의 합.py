n = int(input())
s = list(map(int, input().split()))

s = sorted(s)
tmp = 0
for i in s:
    if tmp + 1 < i:
        break
    tmp += i
    
print(tmp+1)