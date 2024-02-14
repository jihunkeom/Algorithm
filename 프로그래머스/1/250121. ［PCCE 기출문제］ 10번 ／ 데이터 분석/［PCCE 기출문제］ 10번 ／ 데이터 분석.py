def solution(data, ext, val_ext, sort_by):
    answer = []
    col_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    criterion = col_dict[ext]
    
    for ex in data:
        if ex[criterion] < val_ext:
            answer.append(ex)
    
    answer = sorted(answer, key=lambda x: x[col_dict[sort_by]])
    
    return answer