import sys

input = sys.stdin.readline

t = int(input())

primes = [2]

for i in range(3, 1001):
    flag = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
            flag = False
            continue
    if flag:
        primes.append(i)

for _ in range(t):
    n = int(input())
    flag = False
    for i in primes:
        for j in primes:
            for k in primes:
                if i + j + k == n:
                    flag = True
                    print(i, j, k)
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    
    if not flag:
        print(0)