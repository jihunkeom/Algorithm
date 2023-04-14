def solution(want, number, discount):
    for i in range(len(want)):
        if discount.count(want[i]) < number[i]:
            return 0
        
    answer = 0
    for i in range(0, len(discount)-10):
        flag = True
        items = discount[i:i+10]
        for j in range(len(want)):
            if items.count(want[j]) < number[j]:
                flag = False
                break
        if flag:
            answer += 1
    flag=True
    items = discount[len(discount)-10:]
    for j in range(len(want)):
        if items.count(want[j]) < number[j]:
            flag = False
            break
    if flag:
        answer += 1
    return answer