def solution(numbers, target):
    answer = 0
    queue = [[numbers[0], 0], [-numbers[0], 0]]
    while queue:
        val, idx = queue.pop()
        idx += 1
        if idx < len(numbers):
            queue.append([val + numbers[idx], idx])
            queue.append([val - numbers[idx], idx])
        else:
            if val == target:
                answer += 1
        
    return answer