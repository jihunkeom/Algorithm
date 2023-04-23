def solution(sequence, k):
    answer = []
    min_len = 1000001
    l_p, r_p = 0, 0
    tmp = sequence[l_p]
    while True:
        if (l_p > r_p) or (r_p >= len(sequence)):
            break
        if tmp == k:
            if r_p - l_p < min_len:
                answer = [l_p, r_p]
                min_len = r_p - l_p
                
        if tmp < k:
            r_p += 1
            if r_p >= len(sequence):
                break
            tmp += sequence[r_p]
        else:
            tmp -= sequence[l_p]
            l_p += 1
            if l_p >= len(sequence):
                break
            
        
            
    return answer