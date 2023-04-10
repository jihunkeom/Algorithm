def solution(n):
    fib_seq = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib_seq[i] = fib_seq[i-2] + fib_seq[i-1]
    return fib_seq[-1] % 1234567
    