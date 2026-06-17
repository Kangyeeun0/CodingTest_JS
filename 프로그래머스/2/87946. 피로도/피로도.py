def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)
    
    def dfs(power, cnt) :
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)) :
            if power >= dungeons[i][0] and not visited[i]:
                power -= dungeons[i][1]
                visited[i] = True
                dfs(power, cnt+1)
                ## 체력 감소하고 dfs 이후 돌아올 때 다시 체력 더해줘야 함
                power+=dungeons[i][1]
                visited[i] = False
                
        
    dfs(k,0)
    
    return answer