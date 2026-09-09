def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x:x[1])
    
    # print(routes)
    current = routes[0][1]
    
    answer+=1
    
    for route in routes :
        start, end = route
        
        if start<=current<=end :
            continue
        else :
            current = end
            answer+=1
            
        # print(current)
    
    
    return answer