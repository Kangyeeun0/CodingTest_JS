def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    check = routes[0][1]
    
    for route in routes :
        if route[0] <= check :
            continue
        else :
            check = route[1]
            answer+=1
    return answer