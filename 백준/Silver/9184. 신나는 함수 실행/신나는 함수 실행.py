import sys

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def func(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a > 20 or b > 20 or c > 20:
            return func(20, 20, 20)
        
        if dp[a][b][c] != 0:
            return dp[a][b][c]
        
        elif a < b and b < c:
            dp[a][b][c] = func(a, b, c-1) + func(a, b-1, c) - func(a, b-1, c)
            return dp[a][b][c]
        
        else:
            dp[a][b][c] = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
            return dp[a][b][c]


while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if a == -1 and b == -1 and c == -1:
        break
    
    answer = func(a, b, c)
    print(f"w({a}, {b}, {c}) = {answer}")