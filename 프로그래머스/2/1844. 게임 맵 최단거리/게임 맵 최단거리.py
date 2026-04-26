from collections import deque
def solution(maps):
    answer = 0
    q = deque()
    m = len(maps) # x값
    n = len(maps[0]) # y값
    visited = [[False] * n for _ in range(m)]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q.append((0,0,1))
    visited[0][0] = True
    
    while q :
        x, y, cnt = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<m and 0<=ny<n and maps[nx][ny] == 1 :
                if not visited[nx][ny] : 
                    q.append((nx,ny,cnt+1))
                    maps[nx][ny] = cnt + 1
                    visited[nx][ny] = True
            
    if maps[-1][-1] == 1 :
        return -1
    else :
        return maps[-1][-1]
    return answer