char = list(input().rstrip())

answer = []
for i in range(ord("a"), ord("z")+1):
    if chr(i) in char:
        answer.append(str(char.index(chr(i))))
    else:
        answer.append("-1")
        
print(' '.join(answer))