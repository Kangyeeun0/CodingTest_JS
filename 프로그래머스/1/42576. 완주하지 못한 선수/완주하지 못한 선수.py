def solution(participant, completion):
    answer = ''
    part = {}
    
    for p in participant :
        part[p] = part.get(p, 0) + 1
        

    
    for c in completion :
        if c in part :
            part[c] -= 1
            
            if part[c] == 0 :
                del part[c]
            
            
    # print(part.keys())
    answer = list(part.keys())[0]
    
    
    return answer