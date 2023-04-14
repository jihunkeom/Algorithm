def solution(k, tangerine):
    answer = 0
    tan_cnt = {}
    for x in tangerine:
        if x in tan_cnt:
            tan_cnt[x] += 1
        else:
            tan_cnt[x] = 1
            
    sorted_tan = sorted(tan_cnt.items(), key=lambda x: x[1], reverse=True)
    cnt = 0
    for x in sorted_tan:
        if cnt + x[1] < k:
            cnt += x[1]
            answer += 1
        else:
            answer += 1
            break
        
    return answer