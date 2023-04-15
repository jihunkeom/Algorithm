num = int(input())
data_list = list(map(int, input().split()))
num2 = int(input())
data_list2 = list(map(int, input().split()))

num_set = set()
for x in data_list:
    num_set.add(x)

for x in data_list2:
    if x in num_set:
        print("1")
    else:
        print("0")