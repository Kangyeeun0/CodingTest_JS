def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def game(k, cnt) :
        max_cnt = cnt
        
        for j in range(len(dungeons)) :
            remain, use = dungeons[j]
            if not visited[j] and k >= remain :
                visited[j] = True
                max_cnt = max(max_cnt, game(k-use, cnt+1)) 
                visited[j] = False
                
        return max_cnt

      
    answer = game(k,0)    
    return answer