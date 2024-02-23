import sys

n = int(sys.stdin.readline().rstrip())
dists = list(map(int, sys.stdin.readline().rstrip().split()))
prices = list(map(int, sys.stdin.readline().rstrip().split()))

min_price = prices[0]
answer = 0

for i in range(n-1):
    if prices[i] < min_price:
        min_price = prices[i]
        
    answer += min_price * dists[i]
    
print(answer)