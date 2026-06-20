def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(current, cnt) :
        
        for j in range(n):
            if not visited[j] and computers[current][j] == 1 :
                visited[j] = True
                dfs(j, cnt -1)
                
        return cnt
                
                
                
    for i in range(n) :
        if not visited[i] :
            visited[i] = True
            dfs(i, 1)
            answer+=1
            
    
    
    return answer