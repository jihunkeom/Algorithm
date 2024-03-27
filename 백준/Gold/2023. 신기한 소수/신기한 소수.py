import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

def is_prime(num):
    flag = True
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            flag = False
            break
        
    return flag

primes = []

def find_primes(num):
    if len(str(num)) == n:
        if is_prime(num):
            primes.append(num)
        
        return
        
    if is_prime(num):
        for i in range(10):
            find_primes(10*num + i)
            
find_primes(2)
find_primes(3)
find_primes(5)
find_primes(7)
for x in primes:
    print(x)