def solution(numbers, target):
    answer = 0
    def dfs(idx, result):
        nonlocal answer
        if idx == len(numbers)-1:
            if result == target:
                answer += 1
            return
        else:
            idx += 1
            dfs(idx, result+numbers[idx])
            dfs(idx, result-numbers[idx])
    dfs(-1, 0)
    return answer