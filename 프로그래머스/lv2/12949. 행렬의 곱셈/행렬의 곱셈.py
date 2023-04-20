def solution(arr1, arr2):
    n, m = len(arr1), len(arr2[0])
    answer = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            tmp = 0
            x = arr1[i]
            y = [x[j] for x in arr2]
            # print(x, y)
            for k in range(len(x)):
                tmp += x[k] * y[k]
            answer[i][j] = tmp
    return answer