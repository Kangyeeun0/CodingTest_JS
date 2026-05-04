from collections import deque, defaultdict
def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    max_distance = 0
    
    for v in edge :
        a, b = v
        graph[a].append(b)
        graph[b].append(a)
        
    # print(graph)
    
    distance = [-1] *(n+1)
    distance[1] = 0
    queue = deque()
    queue.append(1)
    
    while queue :
        current = queue.popleft()
        
        for next_node in graph[current] :
            if distance[next_node] == -1 :
                distance[next_node] = distance[current] + 1
                max_distance = max(max_distance, distance[next_node])
                queue.append(next_node)
                
    for d in distance :
        if d == max_distance :
            answer+=1
    return answer