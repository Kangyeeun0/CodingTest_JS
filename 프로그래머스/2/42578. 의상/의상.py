def solution(clothes):
    answer = 1
    closet = {}
    
    for clothe in clothes :
        c, t = clothe
        
        if t not in closet : 
            closet[t] = []
            
        closet[t].append(c)
            
    
    for key, value in (closet.items()):
        # print(value)
        answer *= (len(value)+1)
        
    
    
    
    return answer-1