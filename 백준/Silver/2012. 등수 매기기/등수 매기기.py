import sys

n = int(sys.stdin.readline())
predict = []

for _ in range(n):
    predict.append(int(sys.stdin.readline()))
    
predict = sorted(predict)
tmp = list(range(1, n+1))

answer = 0
for i in range(n):
    answer += abs(predict[i] - tmp[i])

print(answer)