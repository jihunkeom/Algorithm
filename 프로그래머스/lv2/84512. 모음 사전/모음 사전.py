def solution(word):
    tmp = "AEIOU"
    answer = 0
    for a in tmp:
        answer += 1
        if a == word:
            return answer
        for b in tmp:
            answer += 1
            if (a+b) == word:
                return answer
            for c in tmp:
                answer += 1
                if (a+b+c) == word:
                    return answer
                for d in tmp:
                    answer += 1
                    if (a+b+c+d) == word:
                        return answer
                    for e in tmp:
                        answer += 1
                        if (a+b+c+d+e) == word:
                            return answer
    return answer