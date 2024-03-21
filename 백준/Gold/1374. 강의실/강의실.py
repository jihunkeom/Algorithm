import sys
import heapq

input = sys.stdin.readline

n = int(input())

lectures = []
for _ in range(n):
    idx, start, end = map(int, input().split())
    heapq.heappush(lectures, (start, end))
    
classrooms = []
start, end = heapq.heappop(lectures)
heapq.heappush(classrooms, end)
cnt = 1

while lectures:
    start, new_end = heapq.heappop(lectures)
    class_end = heapq.heappop(classrooms)
    
    if start >= class_end:
        heapq.heappush(classrooms, new_end)
    else:
        cnt += 1
        heapq.heappush(classrooms, new_end)
        heapq.heappush(classrooms, class_end)
        
print(cnt)