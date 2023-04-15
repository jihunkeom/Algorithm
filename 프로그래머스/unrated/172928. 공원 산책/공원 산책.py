def solution(park, routes):
    answer = []
    park = [list(x) for x in park]
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                pos = [i, j]
    for route in routes:
        direction, cnt = route.split()
        cnt = int(cnt)
        if (cnt >= len(park)) and (cnt >= len(park[0])):
            continue
            
        if direction == "E":
            if pos[1] + cnt >= len(park[0]):
                continue
            elif "X" in park[pos[0]][pos[1]+1:pos[1]+cnt+1]:
                continue
            else:
                pos[1] += cnt
        elif direction == "W":
            if pos[1] - cnt < 0:
                continue
            elif "X" in park[pos[0]][pos[1]-cnt:pos[1]]:
                continue
            else:
                pos[1] -= cnt
        elif direction == "S":
            if pos[0] + cnt >= len(park):
                continue
            elif "X" in [x[pos[1]] for x in park][pos[0]+1:pos[0]+cnt+1]:
                continue
            else:
                pos[0] += cnt
        elif direction == "N":
            if pos[0] - cnt < 0:
                continue
            elif "X" in [x[pos[1]] for x in park][pos[0]-cnt:pos[0]]:
                continue
            else:
                pos[0] -= cnt
    return pos