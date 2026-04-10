from collections import deque
def solution(maps):
    answer = 0
    visited = [[False] * len(maps[0]) for i in range(len(maps))]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = True
    
    while q :
        x,y, cnt = q.popleft()
        
        if x == len(maps)-1 and y == len(maps[0])-1 :
            break
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) :
                if not visited[nx][ny] and maps[nx][ny] == 1 : 
                    visited[nx][ny] = True
                    maps[nx][ny] = cnt+1
                    q.append((nx,ny, cnt+1))
    
    if maps[-1][-1] == 1 :
        return -1
                             
                             
                             
    return maps[-1][-1]