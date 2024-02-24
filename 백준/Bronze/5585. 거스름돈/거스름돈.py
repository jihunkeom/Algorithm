n = int(input())
cnt = 0
val = 1000 - n

for x in [500, 100, 50, 10, 5, 1]:
    q, r = divmod(val, x)
    cnt += q
    if r == 0:
        break
    val = r
    
print(cnt)