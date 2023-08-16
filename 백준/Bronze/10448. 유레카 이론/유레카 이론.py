t = int(input())
tri_nums = [x*(x+1)//2 for x in range(1, 46)]
eureka = [0 for _ in range(1001)]

for i in tri_nums:
    for j in tri_nums:
        for k in tri_nums:
            if i + j + k <= 1000:
                eureka[i+j+k] = 1

for _ in range(t):
    i = int(input())
    print(eureka[i])