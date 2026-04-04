def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [False] * len(dungeons)
    
    def game(k, count) :
        max_count = count
        
        for i in range(n) :
            need, use = dungeons[i]
            
            if need<=k and visited[i] == False :
                visited[i] = True
                max_count = max(max_count, game(k-use, count+1))
                visited[i] = False
                
        return max_count
                
        
            
    answer= game(k,0)
            
    return answer