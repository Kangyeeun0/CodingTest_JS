def solution(park, routes):
    answer = []
    
    def road(k, current) :
        nonlocal answer
        if k >= len(routes) :
            # print("F", current)
            answer = current
            return current
        
        route = routes[k]
        direction, num = route.split(" ")
        num = int(num)
        current_route = current[:]
        # print(direction, num)
        # print(current)
        
        if direction == "E" :
            for i in range(num) :
                ny = current[1] + 1
                if 0<=ny<len(park[0]) and park[current[0]][ny] != 'X' :
                    current[1] = ny
                else :
                    current = current_route
                    break
        elif direction == "W" :
            for i in range(num) :
                ny = current[1] - 1
                if 0<=ny<len(park[0]) and park[current[0]][ny] != 'X' :
                    current[1] = ny
                else :
                    current = current_route
                    break
        elif direction == 'N' :
            for i in range(num) :
                nx = current[0] - 1
                if 0<= nx < len(park) and park[nx][current[1]] != 'X' :
                    current[0] = nx
                else  :
                    current = current_route
                    break
        elif direction == 'S' :
            for i in range(num) :
                nx = current[0] + 1
                if 0<= nx < len(park) and park[nx][current[1]] != 'X' :
                    current[0] = nx
                else  :
                    current = current_route
                    break
        # print(current)
        road(k+1, current)
    
    
    
    for i in range(len(park)) :
        for j in range(len(park[0])) :
            if park[i][j] == "S" :
                start = [i,j]
                break
                
    # print(start)
    road(0, start)
        
        
    return answer