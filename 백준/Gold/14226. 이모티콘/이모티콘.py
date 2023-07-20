from collections import deque

s = int(input())
log = dict()
log[(1, 0)] = 0

def bfs():
    queue = deque([(1, 0)])
    while queue:
        now, clip = queue.popleft()
        if now == s:
            print(log[(now, clip)])
            break
        
        if (now, now) not in log.keys():
            log[(now, now)] = log[(now, clip)] + 1
            queue.append((now, now))
        if (now+clip, clip) not in log.keys():
            log[(now+clip, clip)] = log[(now, clip)] + 1
            queue.append((now+clip, clip))
        if (now-1, clip) not in log.keys():
            log[(now-1, clip)] = log[(now, clip)] + 1
            queue.append((now-1, clip))
            
bfs()