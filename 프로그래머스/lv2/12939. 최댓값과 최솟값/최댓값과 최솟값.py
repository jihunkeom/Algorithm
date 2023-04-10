def solution(s):
    answer = ''
    nums = [int(x) for x in s.split()]
    min_num = min(nums)
    max_num = max(nums)
    return f"{min_num} {max_num}"