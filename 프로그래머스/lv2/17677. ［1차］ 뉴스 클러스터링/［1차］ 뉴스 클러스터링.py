def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    str1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if len(str1) == 0 and len(str2) == 0:
        answer = 1
        return int(answer * 65536)
    
    # if len(str1) > len(str2):
    #     intersection = [x for x in str2 if x in str1]
    # else:
    #     intersection = [x for x in str1 if x in str2]
    intersection, union = [], []
    for x in set(str1 + str2):
        intersection += ([x] * min(str1.count(x), str2.count(x)))
        union += ([x] * max(str1.count(x), str2.count(x)))
    
    answer = len(intersection) / len(union)
    
    return int(answer*65536)