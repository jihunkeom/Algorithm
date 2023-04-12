def solution(s):
    answer = []
    counter = {}
    s = s.replace("{", "[")
    s = s.replace("}", "]")
    s = eval(s)
    for x in s:
        for val in x:
            if val in counter:
                counter[val] += 1
            else:
                counter[val] = 1
    sorted_counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)
    for x in sorted_counter:
        answer.append(x[0])
    
    return answer