N, X = map(int, input().split())

burger = [1] * 51
patty = [1] * 51 

for i in range(1, N+1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1
    patty[i] = patty[i-1] + 1 + patty[i-1]
    
def go(n, x):
    if n == 0:
        return x
    if x == 1:
        return 0
    
    if x == (burger[n-1] + 2):
        return patty[n-1] + 1
    elif x <= burger[n-1] + 1:
        return go(n-1, x-1)
    elif x <= 2*burger[n-1] + 2:
        return patty[n-1] + 1 + go(n-1, (x-(burger[n-1]+2)))
    else:
        return patty[n]
    
print(go(N, X))