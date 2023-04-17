best = 0
answer = -1
for i in range(5):
    scores = list(map(int, input().split()))
    if sum(scores) > best:
        best = sum(scores)
        answer = i + 1

print(answer, best)