def solution(arr):
    answer = 0
    max_val = max(arr)
    ceil = 1
    for x in arr:
        ceil *= x
    
    for x in range(max_val*2, ceil+1):
        flag = True
        for j in arr:
            if x%j != 0:
                flag = False
                break
        if flag:
            return x
    return answer