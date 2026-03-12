from collections import deque
def solution(maps):
    answer = 0
    n = len(maps[0])
    m = len(maps)
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def bfs(start, target) :
        q = deque()
        visited = [[False] * n for _ in range(m)]
        # print(start)
        x,y = start
        q.append((x,y, 0))
        visited[x][y] = True

        
        while q:
            x,y,d = q.popleft()
            # print(maps[x][y])
            if maps[x][y] == target :
                return d
        
            for k in range(4) :
                nx = x + dx[k]
                ny = y + dy[k]

                if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and maps[nx][ny] != "X" :
                    visited[nx][ny] = True
                    q.append((nx,ny, d+1))
    
        return -1
    
    for i in range(m) :
        for j in range(n) :
            if maps[i][j] == "S" :
                start = (i,j)
            elif maps[i][j] == "L" :
                lever = (i,j)
    
    dist1 = bfs(start, "L")
    dist2 = bfs(lever, "E")
    # print(dist1,dist2)
    
    if dist1 ==-1 or dist2 == -1 :
        return -1
    
    answer = dist1 + dist2
    return answer