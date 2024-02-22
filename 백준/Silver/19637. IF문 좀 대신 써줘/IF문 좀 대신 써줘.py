import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
titles = []
scores = []
characters = []

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    titles.append(a)
    scores.append(int(b))
    
for _ in range(m):
    characters.append(int(sys.stdin.readline().rstrip()))
    
for char in characters:
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if char <= scores[mid]:
            answer = titles[mid]
            end = mid - 1
        else:
            start = mid + 1
            
    print(answer)