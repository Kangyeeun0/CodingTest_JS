def solution(tickets):
    answer = []
    tickets.sort()
    visited = [False] * len(tickets)
    # print(tickets)
    
    def dfs(path) :
        if len(path) == len(tickets) + 1 :
            answer.append(path[:])
            # print(answer)
            
        for i in range(len(tickets)) :
            if path[-1] == tickets[i][0] and not visited[i] :
                path.append(tickets[i][1])
                visited[i] = True
                dfs(path)
                # print(path)
                path.pop()
                visited[i] = False

    dfs(['ICN'])
    return answer[0]