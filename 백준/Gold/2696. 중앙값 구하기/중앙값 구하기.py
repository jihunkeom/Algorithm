import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    
    nums = list(map(int, input().split()))
    for i in range(m // 10):
        nums.extend(map(int, input().split()))
    
    med = nums[0]
    left = []
    right = []
    answer = 1
    meds = [nums[0]]
    
    for i in range(1, m):
        tmp = nums[i]
        if tmp < med:
            heapq.heappush(left, -tmp)
        else:
            heapq.heappush(right, tmp)
            
        if i % 2 == 0:
            while len(left) > len(right):
                heapq.heappush(right, med)
                med = -(heapq.heappop(left))
                
            while len(right) > len(left):
                heapq.heappush(left, -med)
                med = heapq.heappop(right)
                
            answer += 1
            meds.append(med)
            
    print(len(meds))
    for i in range(len(meds)):
        if i % 10 == 0 and i != 0:
            print()
        print(meds[i], end=" ")
    print()