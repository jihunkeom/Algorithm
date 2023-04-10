def solution(n):
    answer = 0
    binary_n = format(n, "b").count("1")
    i = n + 1
    while True:
        if i > 0:
            if format(i, "b").count("1") == binary_n:
                return i
            else:
                i += 1
    
    return answer