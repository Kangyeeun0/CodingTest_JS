def solution(brown, yellow):
    answer = []
    width = brown + yellow
    
    for i in range(1, int(yellow**0.5) + 1) :
        if yellow % i == 0 :
            w = yellow // i
            
            W = w + 2
            H = i + 2
            
            if W*H == width :
                return [W, H]
            
        
    
    return answer