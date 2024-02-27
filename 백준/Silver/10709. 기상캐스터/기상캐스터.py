import sys

input = sys.stdin.readline

h, w = map(int, input().rstrip().split())

clouds = []
for _ in range(h):
    cloud = input().rstrip()
    tmp = [x for x in cloud]
    clouds.append(tmp)
    
preds = [["-1"] * w for _ in range(h)]
    
for i in range(h):
    cnt = 0
    flag = False
    for j in range(w):
        if clouds[i][j] == "c":
            preds[i][j] = "0"
            flag = True
            cnt = 0
        elif flag:
            cnt += 1
            preds[i][j] = str(cnt)
            
for x in preds:
    print(" ".join(x))