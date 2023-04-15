n = int(input())

for _ in range(n):
    num_doc, loc = list(map(int, input().split()))
    data_list = list(map(int, input().split()))
    
    answer = 0
    queue = []
    for i in range(len(data_list)):
        queue.append([i, data_list[i]])
        
    # queue = sorted(queue, key=lambda x: x[1], reverse=True)
    while queue:
        x = queue.pop(0)
        if len(queue) == 0:
            print(answer+1)
            break
        
        if x[1] < max([x[1] for x in queue]):
            queue.append(x)
        else:
            answer += 1
            if x[0] == loc:
                print(answer)
                break