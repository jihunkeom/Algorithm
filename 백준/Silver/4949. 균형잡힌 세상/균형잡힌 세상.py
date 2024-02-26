while True:
    line = input()
    if line == ".":
        break
    
    stack = []
    for x in line:
        if x == "(" or x == "[":
            stack.append(x)
        
        elif x == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop(-1)
            else:
                stack.append("WRONG")
        
        elif x == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop(-1)
            else:
                stack.append("WRONG")
                
    if len(stack) == 0:
        print("yes")
    else:
        print("no")