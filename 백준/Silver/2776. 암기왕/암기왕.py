import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    
    arr1.sort()
    
    for x in arr2:
        start, end = 0, n-1
        flag = False
        while start <= end:
            mid = (start + end) // 2
        
            if arr1[mid] == x:
                flag = True
                break
            elif arr1[mid] > x:
                end = mid - 1
            else:
                start = mid + 1
                
        if flag:
            print(1)
        else:
            print(0)