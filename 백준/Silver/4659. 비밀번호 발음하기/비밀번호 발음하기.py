import sys
from collections import deque

input = sys.stdin.readline

def verify(x):
    vowel_count = 0
    else_count = 0
    prev = None
    vowels = ("a", "e", "i", "o", "u")
    
    consec = deque()
    for k in x:
        if k in vowels:
            vowel_count += 1
        else:
            else_count += 1
        
        if len(consec) > 0 and consec[-1] == k and k not in ("e", "o"):
            return False
        
        if len(consec) >= 3:
            consec.popleft()
        consec.append(k)
        if len(consec) == 3:
            if consec[0] in vowels and consec[1] in vowels and consec[2] in vowels:
                return False
            if consec[0] not in vowels and consec[1] not in vowels and consec[2] not in vowels:
                return False
        
    if vowel_count < 1:
        return False
    return True


while True:
    tmp = input().rstrip()
    
    if tmp == "end":
        break
    
    if verify(tmp):
        print(f"<{tmp}> is acceptable.")
    else:
        print(f"<{tmp}> is not acceptable.")