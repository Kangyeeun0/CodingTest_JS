from collections import deque
def solution(land):
    answer = 0
    visited = [([False] * len(land[0])) for _ in range(len(land))]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    m = len(land[0])
    n = len(land)
    
    # 열별 석유량
    column_sum = [0] * m

    
    for i in range(len(land)) :
        for j in range(len(land[0])) :
            if land[i][j] == 1 and not visited[i][j] :
                q = deque([(i,j)])
                visited[i][j] = True
                
                size = 1
                cols = {j}
                
                while q :
                    # print(q.popleft())
                    x,y = q.popleft()


                    for d in range(4) :
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and land[nx][ny] == 1 :
                                visited[nx][ny] = True
                                q.append([nx,ny])
                                size+=1
                                cols.add(ny)
                
                for col in cols :
                    column_sum[col] += size
    
    return max(column_sum)