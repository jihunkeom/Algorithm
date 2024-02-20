def solution(n, t, m, p):
    answer = ''
    def convert(num, base):
        T = "0123456789ABCDEF"
        q, r = divmod(num, base)
        
        return convert(q, base) + T[r] if q else T[r]
    
    candidate = []
    
    for i in range(t*m):
        conv = convert(i, n)
        candidate.extend(list(str(conv)))
        
    for i in range(p-1, t*m, m):
        answer += candidate[i]
    
    return answer