# dp 문제
def solution(sequence):
    answer = 0
    pulse = []
    
    for i in range(0, len(sequence)) :
        if i % 2 == 1 :
            pulse.append(-sequence[i])
        else :
            pulse.append(sequence[i])
            
    # print(pulse)
            
    max_sum = pulse[0]
    min_sum = pulse[0]
    
    current_max = pulse[0]
    current_min = pulse[0]
    
    for i in range(1, len(pulse)) :
        current_max = max(current_max+pulse[i], pulse[i])
        current_min = min(current_min+pulse[i], pulse[i])
        
        max_sum = max(max_sum, current_max)
        min_sum = min(min_sum, current_min)
    
    return max(max_sum, abs(min_sum))