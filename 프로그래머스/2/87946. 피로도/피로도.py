def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def game(k, cnt) :
        max_count = cnt
        for i in range(len(dungeons)) :
            min_rest, used = dungeons[i]
            if not visited[i] and min_rest<=k :
                k-=used
                visited[i] = True
                max_count = max(max_count, game(k, cnt+1))
                k+=used
                visited[i] = False
            
        return max_count
    
    
    
    answer=game(k,0)
    return answer