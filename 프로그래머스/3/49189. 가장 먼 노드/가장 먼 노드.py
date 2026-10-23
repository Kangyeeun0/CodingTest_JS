from collections import deque
def solution(n, edge):
    answer = 0
    dic = {}
    visited = [False] * (n+1)
    cnt = [0] * (n+1)

    next_node = deque([])
    count = 0
    
    for i in range(1, n+1) :
        dic[i] = []

    
    for v in edge :
        l, r = v
        dic[l].append(r)
        dic[r].append(l)

    
    for value in dic[1] :
        next_node.append([value, count+1])
        visited[value] = True
   
    visited[1] = True
    
    while next_node :
        node, count = next_node.popleft()
        cnt[node] = count
        for value in dic[node] :
            if not visited[value] :
                next_node.append([value, count+1])
                visited[value] = True
        # print(cnt)
        
    max_cnt = max(cnt)
    
    for i in range(len(cnt)) :
        if max_cnt == cnt[i] :
            answer+=1
        
            
            
        
        
    
    
    return answer