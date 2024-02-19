from collections import defaultdict
def solution(survey, choices):
    answer = ''
    scores = defaultdict(int)
    mapping = ["RT", "CF", "JM", "AN"]
    for i in range(len(survey)):
        question = survey[i]
        choice = choices[i]
        
        if choice > 4:
            scores[question[-1]] += choice - 4
        elif choice < 4:
            scores[question[0]] += 4 - choice
            
    for x in mapping:
        a, b = None, None
        if x[0] in scores.keys():
            a = scores[x[0]]
        if x[1] in scores.keys():
            b = scores[x[1]]
        
        if a is not None and b is not None:
            if b > a:
                answer += x[1]
            else:
                answer += x[0]
        elif a is None and b is not None:
            answer += x[1]
        elif b is None and a is not None:
            answer += x[0]
        elif a is None and b is None:
            answer += x[0]
            
    return answer