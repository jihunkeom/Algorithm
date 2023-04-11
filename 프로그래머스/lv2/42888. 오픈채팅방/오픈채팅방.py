def solution(record):
    player_name = dict()
    answer = []
    
    for x in record:
        try:
            action, uid, name = x.split()
        except:
            action, uid = x.split()
            name = player_name[uid]
        player_name[uid] = name      
    
    for x in record:
        action, uid = x.split()[0], x.split()[1]
        if action == "Enter":
            answer.append(f"{player_name[uid]}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{player_name[uid]}님이 나갔습니다.")
    return answer