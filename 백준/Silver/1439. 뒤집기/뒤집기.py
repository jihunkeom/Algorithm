line = input()

cnt0, cnt1 = 0, 0
cur = "a"
for x in line:
    if x != cur:
        if x == "1":
            cnt1 += 1
            cur = "1"
        else:
            cnt0 += 1
            cur = "0"
            
print(min(cnt0, cnt1))