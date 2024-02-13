def solution(n):
    answer = 1000000
    for x in range(1, answer):
        if n % x == 1:
            answer = x
            break
    return answer