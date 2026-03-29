def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    def dfs(k):
        max_count = 0
        
        for i in range(len(dungeons)):
            need, use = dungeons[i]
            
            if not visited[i] and k >= need:
                visited[i] = True
                count = 1 + dfs(k - use)
                max_count = max(max_count, count)
                visited[i] = False
        
        return max_count
    
    return dfs(k)