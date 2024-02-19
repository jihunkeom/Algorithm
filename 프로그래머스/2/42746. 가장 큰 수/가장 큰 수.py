def solution(numbers):
    answer = ""
    numbers = [str(num) for num in numbers]
    
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    answer = str(int("".join(numbers)))
    return answer