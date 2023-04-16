def solution(book_time):
    answer = 0
    room_time = []
    room_info = []
    
    for i in range(len(book_time)):
        start, end = book_time[i]
        start = int(start.split(":")[0])*60 + int(start.split(":")[1])
        end = int(end.split(":")[0])*60 + int(end.split(":")[1])
        room_time.append([start, end])
    room_time = sorted(room_time)
    
    for start, end in room_time:
        if len(room_info) == 0:
            room_info.append([[start, end]])
            continue
        
        flag = False
        for room in room_info:
            res_start, res_end = room[-1]
            if start >= res_end+10:
                room.append([start, end])
                flag = True
                break
        if not flag:
            room_info.append([[start, end]])
    print(room_info)
    answer = len(room_info)
    return answer