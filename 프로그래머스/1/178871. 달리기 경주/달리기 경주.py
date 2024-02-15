def solution(players, callings):
    answer = []
    r2p = {i: player for i, player in enumerate(players)}
    p2r = {player: i for i, player in enumerate(players)}
    
    for i in callings:
        rank = p2r[i]
        player_ahead = r2p[rank-1]
        
        p2r[player_ahead] = rank
        p2r[i] = rank - 1
        
        r2p[rank] = player_ahead
        r2p[rank-1] = i
        
    answer = [r2p[i] for i in range(len(players))]
        
    return answer