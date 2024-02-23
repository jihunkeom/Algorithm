import sys

n = int(sys.stdin.readline())
answer = None
q, r = divmod(n, 5)

if r == 0:
    answer = q
else:
    for x in range(q, -1, -1):
        tmp = n - (5 * x)
        q2, r2 = divmod(tmp, 2)
        if r2 == 0:
            answer = x + q2
            break

if answer is None:
    answer = -1
print(answer)