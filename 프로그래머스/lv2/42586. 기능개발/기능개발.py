import math

def solution(progresses, speeds):
    answer = []
    remain = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    
    tmp = [remain[0]]
    for num in remain[1:]:
        if num <= max(tmp):
            tmp.append(num)
        else:
            answer.append(tmp)
            tmp = [num]
    answer.append(tmp)
    
    return [len(x) for x in answer]