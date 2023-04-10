def solution(s):
    answer = True
    if s[0] != "(":
        return False
    elif s[-1] != ")":
        return False
    elif s.count("(") != s.count(")"):
        return False
    
    stack = list()
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
        
    if len(stack) > 0:
        return False
    
    return answer