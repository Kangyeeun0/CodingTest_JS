def solution(n, computers):
    answer = 0
    visited = [False] * len(computers)
    
    def dfs(current) :
        visited[current] = True
        
        for next_node in range(len(computers)) :
            if computers[current][next_node] == 1 and not visited[next_node] :
                dfs(next_node)
    
    for i in range(len(computers)) :
        if not visited[i] :
            dfs(i)
            answer+=1
    return answer