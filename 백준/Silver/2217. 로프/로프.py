import sys

n = int(sys.stdin.readline())

ropes = []

for _ in range(n):
    rope = int(sys.stdin.readline())
    ropes.append(rope)
    
ropes = sorted(ropes)
answers = []
for x in ropes:
    answers.append(x * n)
    n -= 1
    
print(max(answers))