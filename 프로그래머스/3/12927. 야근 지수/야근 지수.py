import heapq

def solution(n, works):
    total_work = sum(works)
    
    if total_work <= n:
        return 0
    
    # 최대 힙 (음수로 변환)
    heap = [-work for work in works]
    heapq.heapify(heap)
    
    for _ in range(n):
        max_work = -heapq.heappop(heap)
        heapq.heappush(heap, -(max_work - 1))
    
    return sum(work ** 2 for work in heap)