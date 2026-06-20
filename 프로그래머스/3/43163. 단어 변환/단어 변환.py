# DFS 문제인 거 같음
def solution(begin, target, words):
    answer = float('inf')
    visited = [False] * len(words)
    
    if target not in words :
        return 0
    
    
    def dfs(current, cnt) :
        nonlocal answer
        
        if current == target :
            answer = min(answer, cnt)
            return
        
        for i in range(len(words)) :
                if not visited[i]:
                    dif_cnt = 0
                    
                    for j in range(len(current)) :
                        if current[j] != words[i][j] :
                            dif_cnt +=1
                            
                    if dif_cnt == 1:
                        visited[i] = True
                        dfs(words[i], cnt+1)
                        visited[i] = False
                        
                            
                    
                    
        
    dfs(begin, 0)
        
            
    
    
    return answer if answer !=float('inf') else 0