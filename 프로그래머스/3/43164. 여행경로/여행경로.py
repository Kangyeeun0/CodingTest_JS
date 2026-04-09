def solution(tickets):
    answer =[]
    tickets.sort()
    N = len(tickets)
    visited = [False] * N
    
    def dfs(path) :
        
        if len(path) == N + 1 :
            answer.append(path[:])
            return path
        
        for i in range(N) :
            if not visited[i] and tickets[i][0] == path[-1] :
                path.append(tickets[i][1])
                visited[i] = True
                dfs(path)
                path.pop()
                visited[i] = False
    
    
    dfs(['ICN'])
                
    return answer[0]