from collections import deque

n = int(input())

cards = list(range(1, n+1))
cards = deque(cards)

while len(cards) > 1:
    cards.popleft()
    a = cards.popleft()
    cards.append(a)
    
print(cards.popleft())