def solution(phone_book):
    answer = True
    num_set = set()
    for num in phone_book:
        for i in range(len(num)):
            num_set.add(num[:i])
    for num in phone_book:
        if num in num_set:
            return False
    return answer