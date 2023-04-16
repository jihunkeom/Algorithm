def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries, pickups = list(reversed(deliveries)), list(reversed(pickups))
    deliver, pickup = 0, 0
    for i in range(len(pickups)):
        deliver += deliveries[i]
        pickup += pickups[i]
        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            answer += (n-i)*2
        
    return answer