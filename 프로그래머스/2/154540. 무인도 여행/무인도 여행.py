from collections import deque
def solution(maps):
    answer = []
    n = len(maps[0])
    m = len(maps) 
    visitied = [[False] * n for _ in range(m)]
    
    dx= [1,-1,0,0]
    dy= [0,0,1,-1]
    
    def bfs(x,y) :
        q = deque()
        q.append((x,y))
        visitied[x][y] = True
        total = int(maps[x][y])
        
        while q :
            x,y = q.popleft()
            
            for k in range(4) :
                nx = x+dx[k]
                ny = y+dy[k]
                
                if 0<=nx<m and 0<=ny<n and not visitied[nx][ny] and maps[nx][ny] != "X" :
                    visitied[nx][ny] = True
                    q.append((nx,ny))
                    total+=int(maps[nx][ny])
        return total
    
    for i in range(m) :
        for j in range(n) :
            if not visitied[i][j] and maps[i][j] != "X" :
                answer.append(bfs(i,j))
    
    if not answer :
        return [-1]
    

    return sorted(answer)