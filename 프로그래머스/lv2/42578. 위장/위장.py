
def solution(clothes):
    answer = 1
    hash_table = {}
    for val, key in clothes:
        if key not in hash_table:
            hash_table[key] = [val]
        else:
            hash_table[key].append(val)
            
    for key, values in hash_table.items():
        answer *= (len(values) + 1)
        
    return answer - 1