def solution(num):
    arr = [0, 1, 2, 4, 7, 13]
    for i in range(6, num+1):
        arr.append(arr[i-1] + arr[i-2] + arr[i-3])
    
    return arr[num]

T = int(input())

for _ in range(T):
    n = int(input())
    print(solution(n))