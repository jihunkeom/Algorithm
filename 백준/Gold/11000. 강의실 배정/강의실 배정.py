import sys
import heapq

N = int(sys.stdin.readline().rstrip())
lectures = []
for _ in range(N):
    lectures.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
lectures.sort(key=lambda x: x[0])


classes = []
heapq.heappush(classes, lectures[0][1])

for i in range(1, N):
    if lectures[i][0] < classes[0]:
        heapq.heappush(classes, lectures[i][1])
    else:
        heapq.heappop(classes)
        heapq.heappush(classes, lectures[i][1])
        
print(len(classes))