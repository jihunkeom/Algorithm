import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
cards2 = list(map(int, input().split()))

cards.sort()
dic = {}
answer = []

for x in cards:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
        
for y in cards2:
    start, end = 0, n-1
    flag = False
    while start <= end:
        mid = (start + end) // 2
        
        if cards[mid] == y:
            flag = True
            break
        
        elif cards[mid] > y:
            end = mid - 1
        elif cards[mid] < y:
            start = mid + 1
    if flag:
        answer.append(str(dic[y]))
    else:
        answer.append("0")

print(' '.join(answer))