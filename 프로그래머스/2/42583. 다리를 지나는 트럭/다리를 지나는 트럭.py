from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total = 0
    
    while bridge :
        total-=bridge.popleft()
        
        if truck_weights :
            if total + truck_weights[0] <=weight:
                truck = truck_weights.popleft()
                total+=truck
                bridge.append(truck)
            else :
                bridge.append(0)
            
        answer+=1
        # print(bridge)
            
        
            
    
    
    return answer