import heapq

def solution(N, road, K):
    # 그래프 초기화
    graph = [[] for _ in range(N+1)]
    
    # 양방향 그래프 구성
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # 거리 배열 (무한대로 초기화)
    dist = [float('inf')] * (N+1)
    dist[1] = 0  # 시작점
    
    # 우선순위 큐 (거리, 노드)
    heap = []
    heapq.heappush(heap, (0, 1))
    
    while heap:
        current_dist, node = heapq.heappop(heap)
        
        # 이미 더 짧은 거리 있으면 skip
        if current_dist > dist[node]:
            continue
        
        for next_node, cost in graph[node]:
            new_dist = current_dist + cost
            
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    
    # K 이하인 마을 개수
    return sum(1 for d in dist if d <= K)