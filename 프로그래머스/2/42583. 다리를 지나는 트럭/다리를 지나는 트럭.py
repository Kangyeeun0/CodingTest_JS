from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([])
    truck = deque(truck_weights)
    
    for i in range(bridge_length) :
        bridge.append(0)
    
    current_w = 0
    # print(bridge)
    
    while truck :
        b=bridge.popleft()
        current_w -= b
        if current_w + truck[0] <= weight :
            t=truck.popleft()
            bridge.append(t)
            current_w+=t
        else :
            bridge.append(0)
            
        
        answer+=1
        
    while current_w > 0 and bridge :
        b= bridge.popleft()
        current_w -= b
        answer+=1
        
    
    
    return answer