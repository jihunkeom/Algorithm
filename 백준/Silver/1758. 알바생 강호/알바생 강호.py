import sys

n = int(sys.stdin.readline().rstrip())

customers = []
for _ in range(n):
    customers.append(int(sys.stdin.readline().rstrip()))
    

customers = sorted(customers, reverse=True)
answer = 0
for i in range(1, n+1):
    tip = customers[i-1] - (i - 1)
    if tip > 0:
        answer += tip
        
print(answer)