n = int(input())

for _ in range(n):
    password = input()
    lstack, rstack = [], []
    
    for char in password:
        if char == "<":
            if lstack:
                rstack.append(lstack.pop())
        elif char == ">":
            if rstack:
                lstack.append(rstack.pop())
        elif char == "-":
            if lstack:
                lstack.pop()
        else:
            lstack.append(char)
    lstack.extend(reversed(rstack))
    print("".join(lstack))