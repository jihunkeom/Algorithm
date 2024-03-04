import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cnt = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    if word in cnt:
        cnt[word] += 1
    else:
        cnt[word] = 1
    
    
answer = sorted(cnt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for x in answer:
    print(x[0])