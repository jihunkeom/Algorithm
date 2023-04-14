def solution(priorities, location):
    answer = 0
    p_queue = []
    for x in range(len(priorities)):
        p_queue.append([x, priorities[x]])
    
    while p_queue:
        x = p_queue.pop(0)
        if len(p_queue) == 0:
            return len(priorities)
        elif x[1] >= max([a[1] for a in p_queue]):
            answer += 1
            if x[0] == location:
                break
        else:
            p_queue.append(x)
        
    return answer