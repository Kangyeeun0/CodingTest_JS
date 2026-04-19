from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    total_weight = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)  # 다리 위 각 칸의 무게
    
    while bridge :
        time += 1
        
        out = bridge.popleft()
        total_weight -= out
        
        if trucks :
        
            if total_weight+trucks[0] <= weight :
                truck = trucks.popleft()
                bridge.append(truck)
                total_weight += truck
            else :
                bridge.append(0)
            
            
        
        
        
        
        
    return time