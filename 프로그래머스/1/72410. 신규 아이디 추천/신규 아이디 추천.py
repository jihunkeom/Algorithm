def solution(new_id):
    answer = ''
    valid_chars = list(range(ord('A'), ord('Z') + 1))
    valid_chars += list(range(ord('a'), ord('z') + 1))
    valid_chars = [chr(x) for x in valid_chars]
    valid_chars += ["-", "_", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    answer = new_id.lower()
    for x in answer:
        if x not in valid_chars:
            answer = answer.replace(x, "")
    
    while answer.find("..") != -1:
        answer = answer.replace("..", ".")
    
    answer = answer.strip(".")
    
    if len(answer) == 0:
        answer = "a"
    elif len(answer) > 15:
        answer = answer[:15]
    
    answer = answer.rstrip(".")
        
    if len(answer) < 3:
        answer = answer + (answer[-1] * (3 - len(answer)))
    
    
    
    return answer