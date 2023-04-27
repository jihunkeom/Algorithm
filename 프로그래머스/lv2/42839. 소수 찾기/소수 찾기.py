import itertools
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    candidates = set()
    for i in range(1, len(numbers)+1):
        perm = list(itertools.permutations(numbers, i))
        for x in perm:
            candidates.add(int("".join(x)))
    
    for x in candidates:
        if x <= 1:
            continue
        flag = True
        for i in range(2, x//2+1):
            if x % i == 0:
                flag = False
                break
        if flag:
            answer += 1
    
    return answer