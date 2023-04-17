def solution(n):
    answer = 0
    arr = [1, 2]
    for i in range(2, n):
        arr.append((arr[i-1]+arr[i-2]) % 1000000007)
    answer = arr[n-1]
    return answer