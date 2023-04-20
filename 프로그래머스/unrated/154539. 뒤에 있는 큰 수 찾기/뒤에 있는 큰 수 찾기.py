def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        num = numbers[i]
        if len(stack) == 0:
            stack.append((num, i))
            continue
        
        if stack[-1][0] < num:
            while stack:
                if stack[-1][0] >= num:
                    break
                x = stack.pop()
                answer[x[1]] = num
        stack.append((num, i))
                
    return answer