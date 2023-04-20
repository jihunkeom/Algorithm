def solution(elements):
    elem_num = len(elements)
    elements *= 2
    answer = set([x for x in elements])
    for i in range(2, elem_num+1):
        for j in range(len(elements)):
            num = sum(elements[j:j+i])
            answer.add(num)
            
    return len(answer)