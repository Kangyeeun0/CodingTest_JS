def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(k, num) :
        nonlocal answer
        answer = max(num, answer)
        
        if num == len(dungeons) :
            return
        
        for i in range(len(dungeons)) :
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k-dungeons[i][1], num+1)
                visited[i] = False
                
        return 
    
    for i in range(len(dungeons)) :
        if k >= dungeons[i][0] :
            visited[i] = True
            dfs(k-dungeons[i][1], 1)
            visited[i] = False
                
    return answer