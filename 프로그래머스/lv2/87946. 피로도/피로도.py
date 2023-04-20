from itertools import permutations

def solution(k, dungeons):
    candidates = list(permutations(dungeons, len(dungeons)))
    answer = 0
    for candidate in candidates:
        energy = k
        traveled = 0
        for x in candidate:
            if energy == 0:
                break  
            elif energy >= x[0]:
                traveled += 1
                energy -= x[1]
            else:
                continue
        answer = max(answer, traveled)
        
    return answer