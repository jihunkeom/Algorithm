import sys

n = int(sys.stdin.readline().rstrip())

products = []
for _ in range(n):
    products.append(int(sys.stdin.readline().rstrip()))
    
products = sorted(products, reverse=True)
answer = 0
cnt = 0

for i in range(n):
    if cnt == 2:
        cnt = 0
    else:
        answer += products[i]
        cnt += 1
        
print(answer)