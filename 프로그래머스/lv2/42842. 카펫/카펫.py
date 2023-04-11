def solution(brown, yellow):
    maximum = (brown+yellow) // 3
    for i in range(3, maximum+1):
        for j in range(3, maximum+1):
            if i * j > (brown+yellow):
                break
            if i*j == (brown+yellow):
                if (i-2)*(j-2) == yellow:
                    if i >= j:
                        return [i, j]
                    else:
                        return [j, i]
    answer = []
    return answer