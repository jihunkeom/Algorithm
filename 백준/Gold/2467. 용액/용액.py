import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
tmp = 2000000002
answer = [None, None]

for i in range(0, len(arr)):
    A = arr[i]
    start = i+1
    end = len(arr)-1
    
    while start <= end:
        mid = (start + end) // 2
        B = arr[mid]
        
        if A + B == 0:
            print(A, B)
            sys.exit(0)
        
        if abs(A + B) < tmp:
            answer[0] = A
            answer[1] = B
            tmp = abs(A + B)
            
        if A + B > 0:
            end = mid - 1
        else:
            start = mid + 1
            
print(answer[0], answer[1])