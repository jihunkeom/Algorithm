def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 +1):
        tmp = ""
        stack = []
        for j in range(0, len(s), i):
            stack.append(s[j:j+i])
        char = stack[0]
        cnt = 1
        for k in range(1, len(stack)):
            if stack[k] == char:
                cnt += 1
            else:
                if cnt > 1:
                    tmp += f"{cnt}{char}"
                    cnt = 1
                    char = stack[k]
                else:
                    tmp += char
                    char = stack[k]
        if cnt > 1:
            tmp += f"{cnt}{char}"
        else:
            tmp += char
        answer.append(len(tmp))
            
    return min(answer)