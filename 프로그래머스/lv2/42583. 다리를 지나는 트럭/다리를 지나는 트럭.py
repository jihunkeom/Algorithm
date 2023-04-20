from collections import deque

def solution(bridge_length, weight, truck_weights):
    if len(truck_weights) == 1:
        return bridge_length + 1
    
    truck_weights = deque(truck_weights)
    truck = truck_weights.popleft()
    bridge = deque([truck])
    answer = 1
    current_weight = truck
    while truck_weights:
        if len(bridge) == bridge_length:
            current_weight -= bridge.popleft()
            
        answer += 1
        # if sum(bridge)+truck_weights[0] <= weight:
        if current_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
        
    return answer + bridge_length