import sys
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
arr1 = set(arr1)
for x in arr2:
    if x in arr1:
        print(1)
    else:
        print(0)