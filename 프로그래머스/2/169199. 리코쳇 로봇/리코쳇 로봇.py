from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    
    # 시작 위치 찾기
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == "R" :
                start = (i, j)
    
    # 방문 체크
    visited = [[False] * m for _ in range(n) ]
    
    # BFS
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    q = deque([(start[0], start[1], 0)])
    
    # 방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        x, y, cnt = q.popleft()
        
        # 목표 도착
        if board[x][y] == 'G':
            return cnt
        
        for i in range(4):
            nx, ny = x, y
            
            # ⭐ 핵심: 끝까지 미끄러짐
            while True:
                tx = nx + dx[i]
                ty = ny + dy[i]
                
                # 범위 밖 or 장애물 만나면 stop
                if not (0 <= tx < n and 0 <= ty < m) or board[tx][ty] == 'D':
                    break
                
                nx, ny = tx, ty
            
            # 방문 안 했으면
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
    
    return -1