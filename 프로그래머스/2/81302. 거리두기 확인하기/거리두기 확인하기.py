def solution(places):
    answer = []
    
    def check_room(room, x, y) :
        dx= [1,-1,0,0]
        dy = [0,0,1,-1]
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if  0<=nx<5 and 0<=ny<5 :
                if room[nx][ny] == 'P' :
                    return False
        diag = [(1,1), (1,-1), (-1,1), (-1,-1)]
        
        for dx, dy in diag :
            nx = x + dx
            ny = y + dy
            
            if  0<=nx<5 and 0<=ny<5 :
                if room[nx][ny] == 'P' :
                    if room[x+dx][y] != 'X' or room[x][y+dy] !='X' :
                        return False
        
        two_dx = [2,-2,0,0]
        two_dy = [0,0,2,-2]
        
        for i in range(4) :
            nx = x+two_dx[i]
            ny = y+two_dy[i]
            
            if  0<=nx<5 and 0<=ny<5 :
                if room[nx][ny] == 'P' :
                    mid_x = x + two_dx[i] // 2
                    mid_y = y + two_dy[i] // 2
                    if room[mid_x][mid_y] != 'X' :
                        return False
        return True
                        
                          
    
    for i in range(5) :
        is_valid = True
        for j in range(5) :
            for k in range(5) :
                if places[i][j][k] == 'P':
                    check = check_room(places[i], j, k)
                    if not check :
                        is_valid = False
                        break
            if not is_valid :
                break
        
        if is_valid :
            answer.append(1)
        else :
            answer.append(0)
                        
                           
        
    return answer