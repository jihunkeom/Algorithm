def solution(n, words):
    answer = [0, 0]

    for i in range(len(words)):
        per = (i%n) + 1
        if words[i] in words[:i]:
            return [per, i//n+1]
        if i > 0:
            if words[i][0] != words[i-1][-1]:
                return [per, i//n+1]

    return answer