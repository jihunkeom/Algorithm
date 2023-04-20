def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        a, b = i//n, i%n
        a += 1
        b += 1
        answer.append(max(a, b))
    return answer
    