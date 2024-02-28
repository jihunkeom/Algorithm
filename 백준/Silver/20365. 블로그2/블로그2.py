import sys

input = sys.stdin.readline

n = int(input())

colors = input().rstrip()

cnt_1 = colors.count("B")
cnt_2 = colors.count("R")

tmp1 = len([x for x in colors.split("B") if x != ""])
tmp2 = len([x for x in colors.split("R") if x != ""])
if tmp1 >= tmp2:
    answer = 1 + tmp2
else:
    answer = 1 + tmp1
    
print(answer)