T = int(input())

for t in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        a, b = input().split()
        if b in clothes:
            clothes[b].append(a)
        else:
            clothes[b] = [a]
    
    answer = 1
    for key in clothes.keys():
        answer *= (len(clothes[key]) + 1)
        
    answer -= 1
    print(answer)