from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    total_weight = 0
    # print(bridge)
    time = 0
    
    while bridge :
        time +=1
        total_weight -= bridge.popleft()
        
        if truck :
            if total_weight + truck[0] <= weight :
                t = truck.popleft()
                total_weight+=t
                bridge.append(t)
                
            else :
                bridge.append(0)
                
    
    return time