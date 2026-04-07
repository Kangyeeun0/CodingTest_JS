import heapq

def solution(n, works):
    total_work = sum(works)
    answer=0
    
    if total_work <= n:
        return 0
    
    # 최대 힙 (음수로 변환)
    heap = [-k for k in works]
    heapq.heapify(heap)
    # print(heap)
    
    for i in range(n) :
        max_work = -heapq.heappop(heap)
        heapq.heappush(heap, -(max_work-1))
    # print(heap)
    
    for j in range(len(works)) :
        answer += heap[j] **2
        
    return answer