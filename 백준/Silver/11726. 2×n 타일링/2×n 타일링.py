arr = [0, 1, 2, 3, 5]
num = int(input())
for i in range(5, num+1):
    arr.append(arr[i-1] + arr[i-2])
    
print(arr[num] % 10007)