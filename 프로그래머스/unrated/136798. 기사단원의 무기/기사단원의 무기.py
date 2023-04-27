def solution(number, limit, power):
    answer = 0
    # knights = []
    for i in range(1, number+1):
        if i == 1:
            answer += 1
            continue
        tmp = 0
        for j in range(1, int(i**(0.5))+1):
            if i % j == 0:
                if j == (i**(0.5)):
                    tmp += 1
                else:
                    tmp += 2
        # print(i, tmp)
        if tmp > limit:
            tmp = power
        # knights.append(tmp)
        answer += tmp
    return answer