import sys

n, m, p = list(map(int, sys.stdin.readline().split()))

hate_dic = {}
like_dic = {}
visited = [False] * (m+1)

for i in range(n):
    like, hate = list(map(int, sys.stdin.readline().split()))
    tmp = hate_dic.get(hate, -1)
    if tmp == -1:
        hate_dic[hate] = i
        
    like_dic[i] = like

cnt = 0
while True:
    hate_person = hate_dic.get(p, -1)
    if hate_person == -1:
        print(cnt)
        break
    else:
        p = like_dic[hate_person]
        cnt += 1
        
    if visited[p]:
        print(-1)
        break
    
    visited[p] = True