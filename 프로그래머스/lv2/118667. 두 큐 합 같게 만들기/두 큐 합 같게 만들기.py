def solution(queue1, queue2):
    if sum(queue1) == sum(queue2):
        return 0
    answer = 0
    total = sum(queue1 + queue2) // 2
    tmp = sum(queue1)
    queue = queue1 + queue2
    l_pointer, r_pointer = 0, len(queue1)-1
    
    while (l_pointer <= r_pointer) and (r_pointer < len(queue)-1):
        if tmp == total:
            return answer
        elif tmp < total and r_pointer < len(queue):
            r_pointer += 1
            tmp += queue[r_pointer]
        else:
            tmp -= queue[l_pointer]
            l_pointer += 1
        answer += 1
    
    return -1