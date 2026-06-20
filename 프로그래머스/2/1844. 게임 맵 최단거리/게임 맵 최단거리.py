from collections import deque
def solution(maps):
    answer = float('inf')
    n = len(maps) # 행
    m = len(maps[0]) # 열
    visited = [[False] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q= deque()
    
    q.append((0,0,1))
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == n-1 and y == m-1 :
            return cnt
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m :
                if not visited[nx][ny] and maps[nx][ny] == 1 :
                    visited[nx][ny] = True
                    q.append((nx,ny, cnt+1))
    

            
        
    return -1