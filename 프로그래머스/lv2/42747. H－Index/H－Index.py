def solution(citations):
    answers = []
    citations = sorted(citations, reverse=True)
    if citations[0] == 0:
        return 0
    for i in range(1, len(citations)+1):
        answer = 0
        for paper in citations:
            if paper >= i:
                answer += 1
            if answer >= i:
                answers.append(answer)
                break

    return max(answers)