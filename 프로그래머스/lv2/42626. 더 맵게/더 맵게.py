import heapq
def solution(scoville, K):
    # if sum(scoville) < K:
    #     return -1
    
    answer = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return answer
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2*b)
        answer += 1
    if (scoville[0] < K) or (len(scoville) == 0):
        return -1
    return answer