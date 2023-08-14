from itertools import combinations

L, C = map(int, input().split())
letters = list(map(str, input().split()))
letters = sorted(letters)

vowels = ["a", "e", "i", "o", "u"]
# else_letters = [chr(x) for x in range(ord("a"), ord("z")+1) if chr(x) not in vowels]


for candidate in ["".join(x) for x in combinations(letters, L)]:
    vowel_cnt = 0
    else_cnt = 0
    for x in candidate:
        if x in vowels:
            vowel_cnt += 1
        else:
            else_cnt += 1
            
        if vowel_cnt > 0 and else_cnt > 1:
            print(candidate)
            break