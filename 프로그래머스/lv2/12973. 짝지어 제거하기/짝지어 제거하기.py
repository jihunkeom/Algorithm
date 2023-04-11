def solution(s):
    answer = 0
    stack = [s[0]]
    for char in s[1:]:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    if len(stack) == 0:
        return 1
    return answer