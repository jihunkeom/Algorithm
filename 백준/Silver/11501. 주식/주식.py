import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    days = []
    n = int(input())
    days = list(map(int, input().rstrip().split()))
    highest = 0
    answer = 0
    for x in reversed(days):
        if x > highest:
            highest = x
        elif x < highest:
            answer += (highest - x)
    
    print(answer)