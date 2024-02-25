n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))

def solution(cards, m):
    cards = sorted(cards)
    num = 0
    for i in range(len(cards)-2):
        for j in range(i+1, len(cards)-1):
            for k in range(j+1, len(cards)):
                if cards[i] + cards[j] + cards[k] > m:
                    break
                elif (cards[i] + cards[j] + cards[k]) > num:
                    num = cards[i] + cards[j] + cards[k]
                    
    return num

print(solution(cards, m))