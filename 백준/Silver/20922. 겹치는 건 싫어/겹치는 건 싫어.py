import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

num_cnt = [0] * (100001)

idx1 = 0
idx2 = 0
tmp = 1
answer = 1

while idx1 <= idx2:
    if idx2 >= n: break
    
    # print(arr)
    # print(tmp, answer)
    
    val = arr[idx2]
    num_cnt[val] += 1
    
    # print(idx1, idx2, num_cnt[arr[idx2]])
    
    
    if num_cnt[val] > k:
        while num_cnt[val] > k:
            num_cnt[arr[idx1]] -= 1
            idx1 += 1
            tmp -= 1
            # print("WTF", idx1, idx2)
        
    if tmp > answer:
        answer = tmp
    idx2 += 1
    tmp += 1
            
    # print("="*30)
        
print(answer)
        