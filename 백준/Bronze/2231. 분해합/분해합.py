n = int(input())

for i in range(n+1):
    if i + sum([int(x) for x in str(i)]) == n:
        print(i)
        break
    if i == n:
        print(0)