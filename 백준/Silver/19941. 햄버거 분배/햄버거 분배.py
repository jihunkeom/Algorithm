import sys
input = sys.stdin.readline

n, k = map(int, input().split())
line = input()

taken = [False] * n

cnt = 0
for i in range(n):
    if line[i] != "P":
        continue
    
    for j in range(i-k, i+k+1):
        if j < 0 or j >= n:
            continue
        
        if line[j] == "H" and not taken[j]:
            cnt += 1
            taken[j] = True
            break
        
print(cnt)