import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().rstrip().split()))

if k >= n:
    print(0)
    sys.exit()

sensors.sort()

distances = []

for i in range(1, n):
    distances.append(sensors[i] - sensors[i-1])
    
distances.sort(reverse=True)

cnt = 1
for i in range(len(distances)):
    if cnt == (k):
        break
    distances[i] = 0
    cnt += 1
    
print(sum(distances))