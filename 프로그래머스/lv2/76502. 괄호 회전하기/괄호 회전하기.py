def solution(s):
    answer = 0
    for i in range(1, len(s)+1):
        stack = []
        flag = True
        string = s[i:] + s[:i]
        for char in string:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if len(stack) > 0:
                    if char == "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            flag = False
                            break
                    elif char == ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            flag = False
                            break
                    elif char == "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            flag = False
                            break
                else:
                    flag = False
                    break
        if len(stack) == 0 and flag:
            answer += 1
        # print(string, len(stack) == 0 and flag)
    return answer