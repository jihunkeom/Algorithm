from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((numbers[0], 1))
    queue.append((-numbers[0], 1))
    
    while queue:
        num, used = queue.popleft()
        
        if used == len(numbers) and num == target:
            answer += 1
            
        if used < len(numbers):
            for next_num in (num + numbers[used], num - numbers[used]):
                queue.append((next_num, used + 1))
        
    return answer