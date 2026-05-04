from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    
    for road in roads :
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] *(n+1)
    distance[destination] = 0
    
    queue = deque()
    queue.append(destination)
    
    while queue :
        current = queue.popleft()
        
        for next_node in graph[current] :
            if distance[next_node] == -1 :
                distance[next_node] = distance[current] + 1
                queue.append(next_node)
        
    
    # print(graph)
    # print(distance)
    answer = [distance[i] for i in sources]
    
    return answer