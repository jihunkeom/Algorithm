import itertools

heights = []
for _ in range(9):
    heights.append(int(input()))
    
comb = itertools.combinations(heights, 7)
comb = list(comb)

for x in comb:
    if sum(x) == 100:
        answer = x
        
answer = sorted(answer)
for x in answer:
    print(x)