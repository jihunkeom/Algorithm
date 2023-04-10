def solution(people, limit):
    people = sorted(people, reverse=True)
    answer = 0
    idx, r_idx = 0, len(people)-1
    while idx <= r_idx:
        if people[idx] + people[r_idx] > limit:
            answer += 1
            idx += 1
        else:
            idx += 1
            r_idx -= 1
            answer += 1
    
    return answer